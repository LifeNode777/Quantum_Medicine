"""
lifenode_analyzer.py
====================
Reference implementation of the Symplectic Trajectory Reconstruction pipeline
and the ASCALON phase-purity metric (LifeNode Filar II / Module G Zero-Build).

Epistemic notes:
1. Raw theta is scale-dependent. Threshold 0.70 is a CALIBRATION HYPOTHESIS.
2. Two-loop doctrine: diagnostic loop only. Never use in a feedback loop.
3. Negative results are results.

Dependencies: numpy, scipy. Optional: wfdb (for PhysioNet).
License: CC-BY-NC-SA 4.0 - Krzysztof Baran / LifeNode Research Collective.
"""
from __future__ import annotations
import warnings
from dataclasses import dataclass
from typing import Dict, Optional
import numpy as np
from scipy.signal import detrend
from scipy.spatial import cKDTree

__version__ = "1.0.0"
THETA_CRIT_HYPOTHESIS = 0.70

__all__ = [
    "LifeNodeTrajectoryAnalyzer", "ThetaCalibration",
    "analyze_physionet_record", "THETA_CRIT_HYPOTHESIS",
]

def _trapezoid(y: np.ndarray, dx: float) -> float:
    fn = getattr(np, "trapezoid", None) or getattr(np, "trapz")
    return float(fn(y, dx=dx))

def _embed(signal: np.ndarray, tau: int, m: int) -> np.ndarray:
    n = signal.size
    length = n - (m - 1) * tau
    if length <= 0:
        raise ValueError(f"Signal too short: n={n}, (m-1)*tau={(m-1)*tau}.")
    idx = np.arange(length)[None, :] + (np.arange(m) * tau)[:, None]
    return signal[idx].T

def _first_minimum(values: np.ndarray) -> int:
    if values.size < 3: return int(np.argmin(values))
    d = np.diff(values)
    for i in range(1, d.size):
        if d[i - 1] <= 0 < d[i]: return i
    return int(np.argmin(values))

def _mutual_information(x: np.ndarray, y: np.ndarray, bins: int) -> float:
    hist, _, _ = np.histogram2d(x, y, bins=bins)
    p = hist / hist.sum()
    px, py = p.sum(axis=1), p.sum(axis=0)
    mask = p > 0
    joint = np.outer(px, py)
    return float(np.sum(p[mask] * np.log(p[mask] / joint[mask])))

def _autocorrelation(x: np.ndarray) -> np.ndarray:
    x = x - x.mean()
    n = x.size
    fft_len = 1 << (2 * n - 1).bit_length()
    acf = np.fft.irfft(np.abs(np.fft.rfft(x, fft_len)) ** 2, fft_len)[:n]
    if acf[0] == 0: return acf
    return acf / acf[0]

@dataclass
class ThetaCalibration:
    ref_p05: float
    ref_median: float

    @classmethod
    def from_reference(cls, raw_thetas: np.ndarray) -> "ThetaCalibration":
        raw = np.asarray(raw_thetas, dtype=float)
        raw = raw[np.isfinite(raw)]
        if raw.size < 5: raise ValueError("Reference segment too short.")
        return cls(ref_p05=float(np.percentile(raw, 5)), ref_median=float(np.median(raw)))

    def transform(self, theta_raw: np.ndarray) -> np.ndarray:
        denom = self.ref_median - self.ref_p05
        if denom <= 0: return np.full_like(np.asarray(theta_raw, dtype=float), np.nan)
        slope = (0.85 - THETA_CRIT_HYPOTHESIS) / denom
        out = THETA_CRIT_HYPOTHESIS + slope * (np.asarray(theta_raw, dtype=float) - self.ref_p05)
        return np.clip(out, 0.0, 1.0)

class LifeNodeTrajectoryAnalyzer:
    def __init__(self, signal: np.ndarray, sampling_rate: float = 1000.0):
        signal = np.asarray(signal, dtype=float)
        if signal.size < 16: raise ValueError("Signal too short.")
        self.signal = detrend(signal)
        self.sampling_rate = float(sampling_rate)
        self.dt = 1.0 / self.sampling_rate
        self.tau: Optional[int] = None
        self.m: Optional[int] = None
        self.fnn_ratios: list = []

    def optimize_embedding_delay(self, method: str = "mutual_info", max_lag: Optional[int] = None, bins: int = 16) -> int:
        n = self.signal.size
        if max_lag is None: max_lag = min(200, max(10, n // 4))
        if method == "autocorr":
            acf = _autocorrelation(self.signal)
            zero = np.where(np.diff(np.sign(acf)) != 0)[0]
            if zero.size > 0: self.tau = int(max(1, zero[0]))
            else:
                below = np.where(acf < 1.0 / np.e)[0]
                self.tau = int(max(1, below[0])) if below.size else int(max_lag)
            return self.tau
        if method == "mutual_info":
            lags = np.arange(1, max_lag + 1)
            mi = np.empty(lags.size)
            for k, lag in enumerate(lags):
                mi[k] = _mutual_information(self.signal[:-lag], self.signal[lag:], bins)
            self.tau = int(lags[_first_minimum(mi)])
            return self.tau
        raise ValueError(f"Unknown method: {method!r}")

    def optimize_embedding_dimension(self, max_dim: int = 8, tol: float = 0.05, r_tol: float = 10.0) -> int:
        if self.tau is None: raise ValueError("Set tau first.")
        n = self.signal.size
        self.fnn_ratios = []
        chosen = None
        for m in range(1, max_dim + 1):
            if n - m * self.tau < 8: break
            traj = _embed(self.signal, self.tau, m)
            length = n - m * self.tau
            traj = traj[:length]
            next_coord = self.signal[m * self.tau: m * self.tau + length]
            tree = cKDTree(traj)
            dist, idx = tree.query(traj, k=2)
            d_m = dist[:, 1]
            valid = d_m > 1e-12
            if not np.any(valid):
                self.fnn_ratios.append(1.0)
                continue
            nn = idx[:, 1][valid]
            ratio = np.abs(next_coord[valid] - next_coord[nn]) / d_m[valid]
            frac = float(np.mean(ratio > r_tol))
            self.fnn_ratios.append(frac)
            if m >= 2 and frac < tol:
                chosen = m
                break
        self.m = chosen if chosen is not None else max_dim
        return self.m

    def reconstruct(self, tau: Optional[int] = None, m: Optional[int] = None) -> np.ndarray:
        tau = tau or self.tau
        m = m or self.m
        if tau is None or m is None: raise ValueError("Set tau and m first.")
        return _embed(self.signal, int(tau), int(m))

    def calculate_ascalon_purity(self, trajectory: Optional[np.ndarray] = None, curvature: str = "accel") -> float:
        traj = trajectory if trajectory is not None else self.trajectory_safe()
        if traj is None or traj.shape[0] < 3:
            warnings.warn("Trajectory too short; theta=NaN.", RuntimeWarning)
            return float("nan")
        v = np.gradient(traj, self.dt, axis=0)
        a = np.gradient(v, self.dt, axis=0)
        speed = np.linalg.norm(v, axis=1)
        if curvature == "accel":
            kappa = np.linalg.norm(a, axis=1)
        elif curvature == "frenet":
            v2 = np.sum(v * v, axis=1)
            a2 = np.sum(a * a, axis=1)
            va = np.sum(v * a, axis=1)
            cross2 = np.clip(v2 * a2 - va * va, 0.0, None)
            kappa = np.sqrt(cross2) / np.clip(speed ** 3, 1e-12, None)
        else:
            raise ValueError(f"Unknown curvature mode: {curvature!r}")
        num = _trapezoid(kappa * speed, self.dt)
        den = _trapezoid(speed ** 2, self.dt)
        return float(num / den) if den > 0 else float("nan")
            def trajectory_safe(self) -> Optional[np.ndarray]:
        if self.tau is None or self.m is None: return None
        try: return self.reconstruct()
        except ValueError: return None

    def sliding_window_analysis(self, window_size: int = 300, step_size: int = 60,
                                curvature: str = "accel", threshold_mode: str = "relative",
                                beta: float = 0.70, calibration: Optional[ThetaCalibration] = None) -> Dict[str, np.ndarray]:
        if self.tau is None or self.m is None: raise ValueError("Set tau and m first.")
        n = self.signal.size
        times, thetas = [], []
        for start in range(0, max(1, n - window_size), step_size):
            window = self.signal[start:start + window_size]
            theta = float("nan")
            if window.size > (self.m - 1) * self.tau + 3:
                sub = LifeNodeTrajectoryAnalyzer(window, self.sampling_rate)
                traj = sub.reconstruct(tau=self.tau, m=self.m)
                theta = sub.calculate_ascalon_purity(traj, curvature=curvature)
            times.append(start / self.sampling_rate)
            thetas.append(theta)
        thetas = np.asarray(thetas, dtype=float)
        times = np.asarray(times, dtype=float)
        baseline = float(np.nanmedian(thetas)) if np.isfinite(thetas).any() else float("nan")
        if threshold_mode == "relative":
            if not np.isfinite(baseline) or baseline <= 0:
                warnings.warn("Degenerate baseline.", RuntimeWarning)
                thr = np.full_like(thetas, np.nan)
            else: thr = np.full_like(thetas, beta * baseline)
        elif threshold_mode == "absolute":
            if calibration is None:
                warnings.warn("Absolute mode without calibration!", RuntimeWarning)
                thr = np.full_like(thetas, THETA_CRIT_HYPOTHESIS)
            else:
                thr = np.full_like(thetas, THETA_CRIT_HYPOTHESIS)
                thetas = calibration.transform(thetas)
        else: raise ValueError(f"Unknown threshold_mode: {threshold_mode!r}")
        drift = np.zeros(thetas.size, dtype=bool)
        for i in range(2, thetas.size):
            recent = thetas[i - 2:i + 1]
            r_thr = thr[i - 2:i + 1]
            if np.all(np.isfinite(recent)) and np.all(np.isfinite(r_thr)):
                drift[i] = bool(np.all(recent < r_thr))
        return {"time": times, "theta": thetas, "threshold": thr, "drift_detected": drift}

def analyze_physionet_record(record_name: str, window_seconds: float = 60.0,
                             step_seconds: float = 12.0, sampto: Optional[int] = None, **drift_kwargs) -> Dict:
    try: import wfdb
    except ImportError as exc: raise ImportError("wfdb required") from exc
    record = wfdb.rdrecord(record_name, sampto=sampto) if sampto else wfdb.rdrecord(record_name)
    annotation = wfdb.rdann(record_name, "atr")
    signal = record.p_signal[:, 0]
    fs = float(record.fs)
    analyzer = LifeNodeTrajectoryAnalyzer(signal, fs)
    analyzer.optimize_embedding_delay()
    analyzer.optimize_embedding_dimension()
    results = analyzer.sliding_window_analysis(window_size=int(window_seconds * fs),
                                               step_size=int(step_seconds * fs), **drift_kwargs)
    drift = results["drift_detected"]
    onsets = np.where(drift[1:] & ~drift[:-1])[0] + 1
    onset_times = results["time"][onsets]
    annotation_times = annotation.sample / fs
    lead_times = []
    for ann_t in annotation_times:
        pos = np.searchsorted(onset_times, ann_t)
        if pos > 0: lead_times.append(float(ann_t - onset_times[pos - 1]))
    return {
        "record": record_name, "fs": fs, "tau": analyzer.tau, "m": analyzer.m,
        "theta_mean": float(np.nanmean(results["theta"])), "theta_std": float(np.nanstd(results["theta"])),
        "drift_percentage": float(100 * np.mean(drift)), "n_annotations": int(len(annotation_times)),
        "avg_lead_time_seconds": float(np.mean(lead_times)) if lead_times else 0.0,
        "sensitivity": (len(lead_times) / len(annotation_times) if len(annotation_times) else 0.0),
        "results": results,
    }

def _demo() -> None:
    rng = np.random.default_rng(42)
    fs = 100.0
    t = np.arange(0, 600, 1 / fs)
    regime_a = np.sin(2*np.pi*0.5*t) + 0.5*np.sin(2*np.pi*1.0*t+0.7) + 0.1*rng.normal(size=t.size)
    regime_b = 0.15*np.sin(2*np.pi*0.5*t) + 0.8*rng.normal(size=t.size)
    signal = np.concatenate([regime_a, regime_b])
    analyzer = LifeNodeTrajectoryAnalyzer(signal, fs)
    tau = analyzer.optimize_embedding_delay()
    m = analyzer.optimize_embedding_dimension()
    print(f"tau={tau}, m={m}")
    half = len(signal) // 2
    for name, seg in (("A", signal[:half]), ("B", signal[half:])):
        sub = LifeNodeTrajectoryAnalyzer(seg, fs)
        sub.tau, sub.m = tau, m
        print(f"regime {name}: raw theta = {sub.calculate_ascalon_purity():.4f}")
    res = analyzer.sliding_window_analysis(window_size=int(60*fs), step_size=int(12*fs))
    print(f"drift-flagged: {100*np.mean(res['drift_detected']):.1f}%")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        out = analyze_physionet_record(sys.argv[1])
        for k, v in out.items():
            if k != "results": print(f"{k}: {v}")
    else: _demo()
