### Topic 2: Emcee and Pantheon+ Parameter Inference

Data used: [Pantheon+SH0ES](https://github.com/PantheonPlusSH0ES/DataRelease/tree/main/Pantheon%2B_Data/4_DISTANCES_AND_COVAR) supernova sample. The analysis follows a simplified version of [Brout et al. 2022](https://arxiv.org/pdf/2202.04077).

---

#### `pantheon_test_curves.ipynb`
Sanity check notebook to verify the theoretical model and data are consistent before running inference.
1. Load Pantheon+SH0ES data and apply basic cuts (`z > 0.01`, exclude Cepheid calibrators)
2. Define the theoretical distance modulus `μ(z)` for flat ΛCDM using `astropy`
3. Plot the Hubble diagram: data vs. theoretical curves for several `(H₀, Ωₘ)` combinations
4. Explore the effect of varying `H₀` and `Ωₘ` separately

---

#### `pantheon_inference.ipynb`
Main inference notebook. Runs `emcee` MCMC chains for four cosmological models using the Tripp (1998) distance estimator with nuisance parameters `(α, β, M)` inferred simultaneously. Statistical errors only; `δ_bias = δ_host = 0`.
1. Load data and define shared functions: Tripp estimator, `σ_μ`, log-likelihood, sampler, and convergence diagnostics
2. **Flat ΛCDM** — parameters: `(H₀, Ωₘ, α, β, M)`
3. **Curved ΛCDM** — parameters: `(H₀, Ωₘ, Ωk, α, β, M)`
4. **Flat wCDM** — parameters: `(H₀, Ωₘ, w, α, β, M)`
5. **Flat w0waCDM** *(extra)* — parameters: `(H₀, Ωₘ, w₀, wₐ, α, β, M)`
6. Save all chains to `chains/` for use in the comparison notebook

Each model section reports: acceptance fraction, autocorrelation time, Steps/τ, effective sample size, Gelman-Rubin R̂, and a corner plot saved to `plots/`.

---

#### `pantheon_comparison.ipynb`
Results and model comparison notebook. Loads the chains produced by `pantheon_inference.ipynb`.
1. Load chains from `chains/`
2. Summary table: median and 68% CI for all parameters across all models
3. Hubble diagram with posterior predictive lines for all models + residual panel
4. `H₀` and `Ωₘ` comparison across models with error bars
5. Overlaid `H₀`–`Ωₘ` posterior contours (68% and 95%)
6. Dark energy constraints: marginal posterior on `w` (wCDM) and `w₀`–`wₐ` plane (w0waCDM)

#### `emcee_tutorial.ipynb`
Runs the official [emcee line-fitting tutorial](https://emcee.readthedocs.io/en/stable/tutorials/line/) as-is to verify the installation and understand the workflow before applying it to real data.

---

#### `emcee_line.ipynb`
Applies the emcee line-fitting workflow to `data/line-1.dat` and `data/line-2.dat` (format: 3 rows — x, y, σ_y).
1. Load both datasets
2. Define the model: linear fit `y = mx + b` with a nuisance parameter `log(f)` to account for underestimated errors
3. Find the Maximum Likelihood Estimate (MLE) with `scipy.optimize` as the starting point for the walkers
4. Run `emcee` with 32 walkers using `DEMove` and `DESnookerMove` for robust exploration
5. Trace plots and autocorrelation time → automatic burn-in and thinning
6. Corner plots with 16/50/84 percentiles for both datasets
7. Hubble diagram: data with error bars, posterior predictive band, and true line
8. Convergence diagnostics: acceptance fraction, τ, Steps/τ, effective sample size, and Gelman-Rubin R̂

All figures are saved to `plots/`.


### Findings

- When using the nuisance parameter for the line-1.dat data the system pushes logf -> -inf, which gives doesn't allow the walker to explore correctly the parameter space. The solution is to reset the position of logf inside the prior interval. This effect is due to the almost perfect agreement of data to the model indicating that for this problem there's is no need of this nuisance parameter.
- TODO: The cuts in the contours seem to be related to the *prior*. For example, in OmM we can change the prior from $0.05<OmM<0.7$ to $-0.05<OmM<0.7$ such that the cut does not appear.
- 
