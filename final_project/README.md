# Bayesian inference on the Planck 2018 binned TT power spectrum

Final project for the *Advanced Data & Statistical Methods Laboratory*.

We fit the publicly released Planck 2018 **binned** temperature (TT) angular
power spectrum with a CAMB theoretical model, a simplified per-bin Gaussian
likelihood (with a Gaussian prior on the optical depth τ), and MCMC sampling
with `emcee`, recovering the six base ΛCDM parameters.

## Structure

```
planck_bayes/
├── planck_model.py          # compute engine: data loading, CAMB theory, priors, likelihood
├── planck_inference.ipynb   # notebook: runs the analysis and produces all figures (Steps 1–7)
├── report.tex               # LaTeX report (Option 1)
├── requirements.txt         # pinned dependencies
├── data/                    # Planck binned TT file (auto-downloaded on first run)
├── figures/                 # figures produced by the notebook
└── chains/                  # saved MCMC chain, log-prob and progress log
```

The model and likelihood live in `planck_model.py` (not inline in the notebook)
so the MCMC worker processes can import them under the `spawn` start method —
required on macOS, where forking an active OpenMP runtime (OpenBLAS / CAMB)
deadlocks.

## Running

```bash
pip install -r requirements.txt
jupyter lab                 # open planck_inference.ipynb and run top-to-bottom
```

The first run downloads the Planck data file automatically. Step 4 (sampling) is
the slow part; while it runs, monitor progress from another cell with
`!tail -n 8 chains/progress.log`.

## Method (brief)

- **Data:** `COM_PowerSpect_CMB-TT-binned_R3.01.txt` (Planck PR3 ancillary data).
- **Theory:** CAMB `D_ℓ^TT`, interpolated to the data multipoles.
- **Likelihood:** diagonal Gaussian (per-bin variance only).
- **Parameters:** Ω_b h², Ω_c h², H₀, τ, ln(10¹⁰A_s), n_s, with a Gaussian τ prior.
- **Sampler:** `emcee` (affine-invariant ensemble), parallelised over walkers.

## AI use

This project was developed with the assistance of the AI model **Claude
(Anthropic)**, used to help structure the code and report and to debug the
parallel sampler. All code was reviewed and executed by the author, and all
scientific choices are the author's own. The prompts that reproduce each step are
logged in Appendix A of `report.tex`.
