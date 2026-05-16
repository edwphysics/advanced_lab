# Topic 3: Cosmological Parameter Inference with PyMultiNest

Bayesian inference of cosmological parameters using the Pantheon+SH0ES supernova sample
([Brout et al. 2022](https://arxiv.org/pdf/2202.04077)), following a simplified version of the
official analysis. Results are compared against the emcee MCMC chains from Topic 2.

---

## Notebooks

| Notebook | Description |
|---|---|
| `pantheon_multinest.ipynb` | Runs PyMultiNest for all four cosmological models |
| `pantheon_comparison_full.ipynb` | Compares emcee vs MultiNest posteriors; AIC, BIC, Bayes factors |

Chains and evidence values are saved to `chains/`. Figures are saved to `plots/`.

---

## Data

- **`data/Pantheon+SH0ES.dat`** — 1701 SNe Ia with SALT2 light-curve parameters
- **`data/Pantheon+SH0ES_STATONLY.cov`** — N×N statistical covariance matrix (N=1701)

Applied cuts: `zHD > 0.01` and `IS_CALIBRATOR == 0` (excludes Cepheid host calibrators).

---

## Model

Distance modulus from the Tripp (1998) estimator (Eq. 1, Brout+2022):

$$\mu_{\rm obs} = m_B + \alpha x_1 - \beta c - M$$

with $\delta_{\rm bias} = \delta_{\rm host} = 0$ (statistical analysis only).

**$M$ is fixed** to $M = -19.253$ mag from the SH0ES Cepheid calibration (Riess et al. 2022,
arXiv:2112.04510). Without an external distance anchor, $H_0$ and $M$ are perfectly degenerate
and neither can be constrained from SNe Ia alone.

Theoretical distance modulus for flat ΛCDM (Eq. 11):

$$\mu_{\rm model}(z) = 5\log_{10}(d_L(z) / 10\,{\rm pc})$$

computed with `astropy.cosmology`.

---

## Likelihood

Full covariance matrix likelihood (Eq. 9, Brout+2022):

$$-2\ln\mathcal{L} = \Delta\vec{D}^T\, C_{\rm stat}^{-1}\, \Delta\vec{D} + \ln\det(2\pi C_{\rm stat})$$

where $\Delta D_i = \mu_{{\rm obs},i} - \mu_{{\rm model}}(z_i)$.

> **Important**: both emcee and MultiNest use this same likelihood. An earlier version of the
> emcee notebook used diagonal errors from SALT2 error propagation instead of the full covariance
> matrix, which produced systematically different posteriors — most visibly in $\beta$ (~2.5 vs ~3.1).
> This was corrected by loading and inverting `STATONLY.cov` in both notebooks.

---

## Priors

Uniform (flat) priors for all parameters — same in both emcee and MultiNest:

| Parameter | Prior range | Description |
|---|---|---|
| $H_0$ | (50, 100) km/s/Mpc | Hubble constant |
| $\Omega_m$ | (0.05, 0.70) | Matter density |
| $\Omega_k$ | (−0.5, 0.5) | Curvature (curved ΛCDM only) |
| $w$ | (−3.0, 0.0) | DE equation of state (wCDM) |
| $w_0$ | (−3.0, 0.0) | Present-day DE EoS (w0waCDM) |
| $w_a$ | (−3.0, 3.0) | DE EoS evolution (w0waCDM) |
| $\alpha$ | (0.0, 1.0) | SALT2 stretch nuisance |
| $\beta$ | (1.0, 5.0) | SALT2 color nuisance |

In MultiNest, priors are implemented as mappings from the unit hypercube $[0,1]^n$ to the
physical ranges above.

---

## Models compared

| Model | Free parameters | $k$ |
|---|---|---|
| Flat ΛCDM | $H_0, \Omega_m, \alpha, \beta$ | 4 |
| Curved ΛCDM | $H_0, \Omega_m, \Omega_k, \alpha, \beta$ | 5 |
| Flat wCDM | $H_0, \Omega_m, w, \alpha, \beta$ | 5 |
| Flat w0waCDM | $H_0, \Omega_m, w_0, w_a, \alpha, \beta$ | 6 |

---

## Model comparison metrics

**AIC** and **BIC** use the maximum likelihood from the emcee chains:

$$\text{AIC} = 2k - 2\ln\mathcal{L}_{\rm max}, \qquad \text{BIC} = k\ln N - 2\ln\mathcal{L}_{\rm max}$$

**Bayes factors** use the log-evidence $\ln\mathcal{Z}$ computed by MultiNest.
Interpretation follows the Jeffreys scale: $|\Delta\ln Z| < 1$ inconclusive, 1–2.5 moderate,
2.5–5 strong, >5 decisive.

The reference model for $\Delta$AIC, $\Delta$BIC, and $\Delta\ln Z$ is **Flat ΛCDM**
(sent first to MultiNest as the baseline).

---

## Things to improve and investigate

- **MultiNest runs in seconds, emcee takes hours** — MultiNest uses nested sampling which is
  inherently more efficient for evidence calculation and handles multimodal posteriors better.
  emcee uses MCMC ensemble sampling which requires many steps to decorrelate, especially when
  parameters are correlated (e.g., $H_0$–$\Omega_m$). A fair speed comparison should note that
  MultiNest with `n_live=400` gives fewer effective samples than emcee with 8000 steps × 64 walkers.

- **Hard edges in MultiNest contours** — the cuts visible in the 2D marginal contours (especially
  for $\Omega_m$ and $w$) are caused by the prior boundaries being hit by the posterior. This means
  the prior is too tight in those directions and should be widened, or the parameter is genuinely
  prior-dominated in that region. Investigate by rerunning with wider priors and checking if the
  edge disappears.

- **Use `STAT+SYS` covariance** — currently only statistical uncertainties are included.
  The full `Pantheon+SH0ES_STAT+SYS.cov` includes systematic covariances between SNe and
  Cepheid hosts, which is what the paper uses.

- **Include $\delta_{\rm bias}$ and $\delta_{\rm host}$** — both correction terms are set to zero.
  The bias corrections are provided per SN in the data file; the host-mass step (Eq. 2) requires
  the host stellar mass column `HOSTGAL_LOGMASS`.

- **Increase `n_live` in MultiNest** — currently set to 400. The paper uses PolyChord with
  250 live points and 30 repeats. Increasing `n_live` improves the accuracy of $\ln\mathcal{Z}$
  and the shape of the posterior tails, at the cost of runtime.

- **Add external probes** — combine with CMB ($\Omega_m h^2$ prior from Planck) and BAO to
  break the $H_0$–$\Omega_m$ degeneracy, as done in Section 4 of Brout+2022.

- **Validate $w_0$–$w_a$ results** — the w0waCDM posterior shows large uncertainties and possible
  prior dependence in $w_a$. SNe Ia alone have limited constraining power on $w_a$; this model
  requires BAO or CMB data to be well constrained.