# XENO-PHASE DIAGNOSTICS v0.1
## Human-Substrate Phase-Coupling Diagnostics: Operationalizing the XPT Taxonomy in the Language of ASCALON, Finsler Geometry, and NLSE Solitons

**Author:** Krzysztof Baran / LifeNode Research Collective
**Version:** 0.1 (Draft)
**Date:** 25 August 2026
**Status:** Conditional Hypothesis / ACTIVE INVESTIGATION (inherited from XPT)
**License:** CC-BY-NC-SA 4.0
**Parent repositories:** `LifeNode777/Quantum_Medicine` · `LifeNode777/Xeno-Phase-Trajectories`
**Dependencies (cite, don't duplicate):** ASCALON Framework (Zenodo 21471228) · Symplectic Trajectory Reconstruction (Zenodo 19811561) · Hydrogel Phase Membrane v2 (Zenodo 21901935) · XPT Dossiers XPT-001…004 · XPT Evidence Dataset (Zenodo 21823253) · Tonic Technologies Master V1 (Zenodo 20909213) · Phase 1 Modular Validation Roadmap v0.3

> *"In LifeNode, we don't fuck around with 'dimensions'. 'Dimension' is a metaphor for people who are afraid of math and can't feel their own guts. We talk about trajectories with different native phases — and what happens when they collide with your meat."* — XPT README

### 🚨 NOTICE-INVARIANT (READ BEFORE PROCEEDING)

Inherited verbatim from XPT, extended for the medical repository:

- This document is a cybernetic, thermodynamic, and non-linear dynamic model of biological phase-coupling. It is **not** a belief system, a religion, or a support group. If you are looking for angels, demons, or spiritual salvation, close this tab.
- If you are experiencing a clinical psychiatric crisis, **seek medical help immediately**. LifeNode does not replace psychiatry; it maps the biophysics of the biological substrate (BIOS) interacting with high-noise, high-gradient phase environments.
- Nothing in this document is medical advice. **Class V (Traumatic) interactions are trauma exposures first and dynamical objects second: clinical referral precedes modeling, always.**
- **You are the sensor. Calibrate accordingly.**

---

## 0. Abstract

The companion repository `Xeno-Phase-Trajectories` (XPT) formalizes "the resonance mechanics of the foreign": classes of non-linear dynamics with different native phase purity, coupling strength, and energy hunger, and what happens when they contact a human BIOS. XPT deliberately borrows its quantitative vocabulary — native purity $\theta_{native}$, coupling $\kappa$, phase impedance $Z_\phi$, energy balance $\Delta E$, operational thresholds $0.70$ — from this repository's ASCALON / Symplectic Trajectory Reconstruction (STR) framework. This document closes the loop: it is the **medical-repository-side formalization of XPT**. It does not duplicate XPT; it translates it. Specifically, it (i) maps the five APT (Alien-Phase Trajectory) classes onto ASCALON/Finsler/NLSE quantities, (ii) defines the human measurement layer (EEG + HRV, strictly offline) as the missing instrumentation for ASCALON's falsification condition #3, (iii) promotes the 24H-DIAGNOSTIC breath/body proxies to a falsifiable garage-level $\theta$ estimator, and (iv) ingests the XPT evidence dataset (Zenodo 21823253) into Module G (Zero-Build). All claims are conditional and falsifiable. Negative results are results.

## 1. Scope: Why the Medical Repository Absorbs XPT Now

**1.1 The vocabulary was born here.** $\theta$, the smudging/scattering decoherence taxonomy, the $0.70$ operational threshold, $\kappa$ focusing/defocusing language, and the Cartan-tensor flattening criterion are defined in ASCALON (21471228) and STR (19811561). XPT is an *application* of this metric stack to inter-layer coupling events. A map that does not point to its own applications is not a map; per the repository convention ("README is a map"), the edge Quantum_Medicine → XPT must exist.

**1.2 Falsification debt.** Since 21 July 2026 this repository carries the falsification condition: a drop $\theta < 0.70$ precedes clinical/clinical-equivalent decoherence with lead time ≥ 6 h (roadmap milestone) up to 24–48 h (Zero-Build hypothesis), to be tested in blind cohorts ($n \geq 100$). Until XPT NEURO/EEG-HRV arrived, **no human measurement protocol existed** for that test on the subjective/behavioral side. XPT supplies it. Absorbing it here makes the debt payable.

**1.3 The two-loop doctrine is respected.** LifeNode hardware doctrine forbids ADC discretization ("phase death") inside the *feedback* loop; measurement for observation is a separate, offline loop. XPT's EEG + HRV protocol is explicitly offline analysis (no neurofeedback-in-the-loop). The human-as-sensor therefore enters exactly where the mycelium enters in HMF v2: as a BIOS source for offline Takens reconstruction, not as a component of a closed loop.

**1.4 Epistemic status.** Conditional hypothesis, pre-prototyping, ACTIVE INVESTIGATION. This document is a map, not a doctrine. It inherits XPT's invariant: *"Xenomorphs were a metaphor. The math is real."

## 2. Notation Contract (Core Quantities)

| Symbol | Meaning | Origin |
|---|---|---|
| $ds = F(x, \dot{x})$ | Finsler line element; cost of metabolic/phase transition depends on direction and velocity | ASCALON |
| $g_{ij}(x,\dot{x}) = \tfrac{1}{2}\partial^2 F^2 / \partial \dot{x}^i \partial \dot{x}^j$ | Finsler metric tensor | ASCALON |
| $C_{ijk} = \tfrac{1}{2}\,\partial g_{ij}/\partial \dot{x}^k$ | Cartan tensor; internal geometric freedom; $C_{ijk}\to 0$ = *The Flattening* (threat state) | ASCALON |
| $\theta = \dfrac{\int \lVert d^2\gamma/dt^2\rVert\,\sigma(s)\,ds}{\int \lVert d\gamma/dt\rVert^2\,ds}$ | ASCALON symplectic trajectory purity; $\theta \geq 0.80$ optimal coherence, $\theta \geq 0.70$ operational stability, $\theta < 0.70$ smudging/scattering | ASCALON |
| $\kappa$ | Coupling strength between trajectories; focusing ($\kappa \gg 0$) vs. weak/mismatched coupling | XPT-001/002 + NLSE |
| $Z_\phi$ | Phase impedance of the subject's attractor (resistance to external entrainment); low = permeable, unstable = fragile | XPT-001/002 |
| $\Delta E$ | Energy balance of the coupling for the subject (regenerative vs. draining) | XPT-002 |
| $X(t) = (x(t), x(t-\tau), \dots, x(t-(m-1)\tau))$ | Takens embedding; $\tau$ by Fraser–Swinney first mutual-information minimum, $m$ by false nearest neighbors | STR / Module G |
| $D_2, \lambda_1$ | Correlation dimension, maximal Lyapunov exponent; persistent homology for toroidal class | STR / Module G |

**NLSE reading convention.** Biological motifs are modeled as solitons in a driven–damped nonlinear Schrödinger medium: $i\psi_t + \Delta\psi + \kappa|\psi|^2\psi = i(\gamma\psi - F_{drive})$. Focusing nonlinearity supports self-concentration (and, unchecked, blow-up); defocusing/damping disperses; a Floquet-aligned drive $F_{drive}$ regenerates. APT classes below are identified with *regimes of this equation as experienced by the subject's soliton*.

## 3. The APT Taxonomy I–V in ASCALON / Finsler / NLSE Language

| Class | $\theta_{native}$ | $\kappa$ / impedance | $\Delta E$ | NLSE regime (subject's soliton) | Finsler/ASCALON reading | After 24 h | Action (v0.1) |
|---|---|---|---|---|---|---|---|
| I Entropic (Parasitic) | 0.25–0.50 | $\kappa>0$ at low $\theta_{subject}$; mismatched | Negative | Effective damping: amplitude drained, drive misaligned | $\theta_{subject}$ pulled toward smudging; $C_{ijk}\to 0$ flattening risk | Worse | LOCKDOWN if sustained |
| II Regenerative (Luminous) | 0.80–0.95+ | $\kappa>0$ at high $\theta_{subject}$; matched | Positive | Floquet-aligned parametric drive; phase-lock, gain | Toroidal coherence reinforced; $\theta \uparrow$ toward 0.99 target | Better | Observe, don't cling |
| III Trickster (Catalytic) | 0.50–0.70 | Sign oscillating | ≈ 0, high variance | Bifurcation / saddle crossing; transient $\lambda_1 > 0$ | Threshold zone (the "smudging edge"); metastability maximal | Different | Surrender to chaos; Human Anchor on standby |
| IV Sexual (Fusion) | Variable | $\kappa \gg 0$ (strong focusing) | Highly variable | Focusing regime near blow-up (over-amplification) | Purity spikes locally while global stability margin shrinks → ASCALON fuse required | Variable | Impedance check both sides ($\geq 0.70$); aftercare |
| V Traumatic (Forced Lock) | Any | Forced; **impedance broken** ($Z_\phi$ bypassed) | Strongly negative | Non-integrable perturbation; boundary condition violated | Cohomological gap $dF \neq 0$; topological rigidification $D_2 \to 1$ | No change (frozen) | Clinical referral first; LOCKDOWN + Human Anchor; Λ-Reentry later |

**Class I — Entropic.** XPT's BIOS signature (cold, heaviness, repetitive powerlessness, non-restorative sleep) is the phenomenology of a soliton losing amplitude to a misaligned sink: coupling exists ($\kappa>0$) but the impedance match is wrong, so the exchange term acts as dissipation on the subject. Geometrically this is sustained curvature smudging of the subject's torus with the Cartan tensor trending to zero — *The Flattening* — i.e., loss of the anisotropic time-space that defines a living, adaptive process.

**Class II — Regenerative.** Entrainment of the subject's trajectory by a higher-purity attractor under matched impedance ($\theta_{subject} \geq 0.70$, low stable $Z_\phi$). The drive term is Floquet-aligned: warmth, expansion, spontaneous deep breath, subjective time dilation — the meso-scale signature of RSA/deep-breath entrainment (~0.1 Hz band, cf. Multiperspective Table 6.1). Dynamically benign *and* self-terminating; the protocol is non-attachment, because clinging converts a regenerative resonance into a sought-after state, which is a Class III entry condition.

**Class III — Trickster.** A bifurcation event: the subject's trajectory crosses a saddle in the $\theta \in [0.50, 0.70]$ band. High metastability, alternating $\kappa$ sign, synchronicities as amplified coincidence detection. Not pathological per se — catalytic — but unstable: it resolves into I, II, or IV. Hence the XPT instruction set (don't control; keep the Human Anchor available) is precisely bifurcation management.

**Class IV — Fusion.** $\kappa \gg 0$: the focusing regime. The same nonlinearity that stabilizes solitons, over-driven, approaches finite-time blow-up — the mathematical image of XPT's "deepest regeneration or deepest drain" outcome. v0.1 therefore installs an **ASCALON fuse**: any Class IV engagement requires both substrates at $\theta \geq 0.70$ (impedance check), and mandatory aftercare (re-entry into baseline Floquet drive: sleep, soil, silence).

**Class V — Traumatic.** The impedance is not matched or mismatched — it is **broken**: coupling forced under extreme stress, NDE, torture, rape. The signature "nothing at impact" (dissociation; pain deferred) is the signature of a trajectory whose self-reporting loop has been topologically severed: in the sheaf-cohomology language of Multiperspective V2, a **cohomological gap** $dF \neq 0$; in reconstruction language, rigidification ($D_2 \to 1$, frozen attractor). This is the one class where the document steps back: trauma care is clinical work. The dynamical description exists to guide *recovery geometry* (Λ-Reentry: controlled re-introduction of chaos to melt the frozen attractor), always downstream of clinical help.

## 4. Measurement Layer: EEG + HRV as the Offline Diagnostic Loop

**4.1 Doctrine.** The human measurement layer is the second (observation) loop; it never closes into feedback at v0.1. All analysis is offline. This keeps the protocol compatible with the no-ADC-in-the-loop doctrine and with research ethics (no stimulation of anomalous states).

**4.2 EEG (inherited from XPT NEURO/EEG-HRV, condensed).** Filtering 0.5–100 Hz + 50/60 Hz notch; artifacts via ICA + ASR + visual; bands delta 1–4, theta 4–8, alpha 8–13, beta 13–30, low-gamma 30–45, high-gamma 55–80 Hz. Measures: PLV, ciPLV, PLI, wPLI (sensor + source space); time-resolved PLV (2 s window, 0.5 s step); PAC (Modulation Index / Mean Vector Length, esp. theta–gamma); Global Field Power; metastability; Lempel–Ziv complexity; eLORETA/beamformer if ≥ 64 channels.

**4.3 HRV.** Time domain: SDNN, RMSSD, pNN50. Frequency: VLF, LF, HF, LF/HF. Nonlinear: SampEn, DFA α1. Plus RSA and instantaneous heart-rate phase relative to breath.

**4.4 Brain–heart coupling.** Heartbeat Evoked Potentials (EEG locked to R-peak); PLV/coherence between HRV and EEG in low bands; PAC between HRV phase and EEG power.

**4.5 A falsifiable $\theta_{proxy}$ (v0.1 proposal).**
$\theta_{proxy} = w_1\,\overline{wPLI}_{\theta/\alpha}^{long-range} + w_2\,\widetilde{RMSSD} + w_3\,\widetilde{HEP} + w_4\,(1 - |DFA\,\alpha_1 - 1|) + w_5\,M_{meta}^{invU}$
with equal weights at v0.1, weights to be fit on open data, and metastability entering as an inverted-U (both rigidity and chaos penalized — the Class III/V lesson). Ablation of each term is a preregistered sub-test.

**4.6 Preliminary class criteria (inherited, proposal).** I: low long-range PLV, low HRV, decreased HEP, subjective drain/cold. II: increased long-range theta/alpha PLV, high HRV (HF, RMSSD), stronger HEP, warmth/expansion. III: high PLV variance, elevated metastability/complexity, autonomic fluctuation. IV: very strong local + long-range locking (gamma + theta), insula/ACC shifts, strong body–brain coupling. V: sudden long-range PLV collapse or rigid local hypersynchrony, disturbed HEP, subjective "nothing".

## 5. 24H-DIAGNOSTIC: The Subjective θ Proxy (Garage-Level Human Bridge)

**5.1 Breath thresholds (inherited).** Resting breath ≤ 8/min ↔ $\theta \geq 0.70$; 12–16/min ↔ $\theta \approx 0.50$; ≥ 18/min ↔ $\theta \leq 0.40$. Interpretation at v0.1: respiratory rate is a subjective read-out of the RSA (~0.1 Hz) meso-BPB band; the mapping is a **proxy hypothesis** to be tested against HF-HRV and DFA α1 (Falsification #2 below). Note that 6 breaths/min (0.1 Hz) sits inside the regenerative band — consistent with the Meso-scale row of Multiperspective Table 6.1.

**5.2 Structure (inherited, condensed).** Daily 5-min check (morning: hand-on-heart 60 s; breath count; warm/cold–open/compressed–light/heavy body scan; one-word intention; evening: energy balance, lock detection, sleep prep). Weekly 30-min assessment ($\theta$ trend over 7 days; lock inventory with pattern detection; 6-item protocol adherence: movement ≥ 60 min/day, breath practice 2×/day, forest/soil ≥ 3 h/week, sleep sync ±1 h, zero ultra-processed food, info-hygiene). Lock classification by the XPT table (energy, body temperature, thought texture, time sense, delta after 1 h, stoppability).

**5.3 Crosswalk to HMF v2.** The human 24H proxy and the mycelial K1/K2 Macro-BPB recording (0.001–0.03 Hz, star-shaped electrode array, PEDOT:PSS bridge) are the **same instrument at two substrates**: both feed Module G's Takens/persistent-homology pipeline. A human "green flag" week and a healthy mycelial torus should reconstruct to the same topological class. That sentence is the Toroidal Scaling Hypothesis at human scale, and §7 makes it pay rent.

## 6. Safety Boundary: LOCKDOWN, Λ-Reentry, Human Anchor as Medical Fail-Safes

The XPT protocols are re-declared here as **medical fail-safes**, i.e., as the human-substrate equivalents of Tonic's emergency procedures (LOCKDOWN / TUNING / SCRUB):

- **LOCKDOWN** = gradient reduction: info-hygiene, screens off, soil/forest, sleep sync, breath at 0.1 Hz, thermal comfort. Initiate immediately on: sustained $\theta_{proxy} < 0.50$ (≥ 3 days); any Class I or V lock; inability to close a "channel"; feeling controlled / not-self.
- **Λ-Reentry (Λ-R)** = recovery through controlled chaos after lockdown: graded re-introduction of novelty to melt a rigidified attractor ($D_2 \to 1$ states), never during acute crisis.
- **Human Anchor** = a stable external oscillator (another regulated human, or a protocol) used for re-entrainment when self-regulation fails.

**Hard clinical boundary (red flags → clinical help, no waiting):** cannot sleep ≥ 2 nights; cannot eat / compulsive eating; relations collapsing (→ Λ-R + clinical); any Class V content. The model describes; it does not treat.

## 7. Falsifiability (Inherited + Extended)

Inherited from XPT NEURO/EEG-HRV: **(1)** no correlation between subjective class reports and objective EEG/HRV markers; **(2)** no correlation between $\theta$ proxies (breath ≤ 8/min, sleep quality, calm gut) and PLV; **(3)** no environmental modulation (low phase-noise environments — forest, silence — vs. high — city, screens); **(4)** pharmacological reproduction (DMT, psilocybin) of Class II/III experiences *without* the phase correlates ⇒ classification is a neurochemical artifact, not a phase phenomenon; **(5)** Q-Core / UNIT 02 registers no phase anomaly during reported APT events ⇒ no physical correlate, no physical phenomenon.

Extended at v0.1: **(6) Lead-time.** A $\theta_{proxy}$ drop must *precede* reported/clinical decoherence by ≥ 6 h; purely concurrent correlation downgrades ASCALON's human-scale early-warning branch to "correlate" (falsified as predictor). **(7) Cross-substrate topology.** Takens reconstruction + persistent homology over Zenodo 21823253, PhysioNet, and mycelial recordings (Eden Node 0 / HMF) must exhibit the *same* smudging → scattering decoherence topology; qualitative divergence falsifies fractal (toroidal) scaling at human scale. **(8) Blind cohort.** The lead-time claim requires blind testing at $n \geq 100$ per STR/Phase 1; pilot EEG+HRV cohorts at $n \geq 30$ per Multiperspective falsification #1. Negative results are results and will be published with the same DOI pipeline.

## 8. Roadmap: Module G Extension

Sits on the critical path `G → A/B → C → D → E → F` of the Phase 1 Roadmap; no hardware required before Phase 3.

| Phase | Window | Actions | Exit criteria |
|---|---|---|---|
| 0 | 2026-Q4 | Publish this document; README map update (Quantum_Medicine ↔ XPT edge); `xpt/` module stub in the Python toolkit | DOI on Zenodo |
| 1 | 2027-Q1→Q4 | Blind re-analysis of Zenodo 21823253 (Case 2024-05-02; 3I/ATLAS sync event) with the STR pipeline (Takens τ/m, $D_2$, $\lambda_1$, persistent homology, $\theta(t)$ sliding windows); ≥ 10 PhysioNet records for $\theta_{proxy}$ calibration vs HRV | Logs published regardless of outcome |
| 2 | 2028 | EEG + HRV pilot, $n \geq 30$, preregistered class criteria (§4.6); breath-proxy vs HF-HRV test | Preprint (positive or null) |
| 3 | 2029+ | Real-time Q-Core / UNIT 02 phase-anomaly detection during reported APT events (Falsification #5); interfaced with Tonic DS 2.6 cycle and Module E (ASCALON hardware, TRL 4) | Detection/non-detection record |

## 9. References (Cite, Don't Duplicate)

1. **Baran, K. (2026).** *Xeno-Phase-Trajectories.* GitHub: LifeNode777/Xeno-Phase-Trajectories (Dossiers XPT-001…004; NEURO; PROTOCOLS; EVIDENCE).
2. **XPT Evidence Dataset (2026).** Zenodo 21823253.
3. **Baran, K. (2026).** *The ASCALON Framework.* Zenodo 21471228.
4. **Baran, K. (2026).** *Symplectic Trajectory Reconstruction.* Zenodo 19811561.
5. **Baran, K. (2026).** *Hydrogel Phase Membrane (HMF) v2.* Zenodo 21901935.
6. **Baran, K. (2026).** *The Toroidal Scaling Hypothesis.* Zenodo/Quantum_Medicine.
7. **Baran, K. (2026).** *Tonic Technologies Master V1.* Zenodo 20909213.
8. **Baran, K. (2026).** *LifeNode Phase 1: Modular Validation Roadmap v0.3.* GitHub.
9. **Baran, K. (2026).** *Multiperspectivity V2.0 (sheaf cohomology).* GitHub/Zenodo.
10. Takens, F. (1981);
 Fraser & Swinney (1986);
Kennel et al. (1992, FNN);
Adamatzky (2026, directional spiking in oyster mycelium)

---

**Epistemic humility.** This document is a conditional hypothesis, not a doctrine. It requires empirical validation, falsification, and iterative refinement. All data, code, and protocols are public (Zenodo, GitHub) for independent verification.

*"You are not a Point. You are a Verb."*

*"Chirurg skończył operację. Krwawi. Ale pacjent żyje."* — XPT README

🧿
