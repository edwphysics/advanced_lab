# DESI PCA Spectral Templates

Principal Component Analysis of DESI Quasar Spectra

---

## Repository Structure

**notebooks/**
- `desi_spectra_prep.ipynb` - Data preparation & spectra retrieval from DESI-DR1
- `desi_pca.ipynb` - PCA fitting on DESI-DR2 spectra
- `DESI_access_spectra.ipynb` - Tutorial: Loading DESI data
- `astroML_tutorial.ipynb` - Reference implementation from astroML

**data/**
- DESI spectra for PCA fitting

**plots/**
- Generated visualizations (low-z/high-z spectra)

**spec_decompositions.pkl**
- Precomputed spectral decompositions

---

## Key Results

The analysis compares low-redshift and high-redshift quasar populations, constructing spectral templates in the rest frame (RF) for redshift ranges where spectral information is optimally sampled.

---

## Assignment Objectives (Tarea 4)

### 1. Reproduce astroML Examples

Generate the following figures from Chapter 7 of *Statistics, Data Mining, and Machine Learning in Astronomy*:

- **Figure 7.4** - Spectral reconstruction from PCA components
- **Figure 7.5** - Spectral decomposition visualizations
- **Figure 7.6** - Eigenvalue spectrum

**Reference:** [astroML Book Figures – Chapter 7](https://www.astroml.org/book_figures/chapter7/)

### 2. Extend to DESI Data

Reimplement the PCA analysis using contemporary DESI observations of quasars and/or galaxies.

### 3. Construct Spectral Templates

Generate empirical templates suitable for:
- Redshift determination of astronomical objects
- Synthetic data generation
- Classification and analysis pipelines

**Motivating References:**
- [Yip et al. (2023) – AJ, 166, 3](https://iopscience.iop.org/article/10.3847/1538-3881/ace35d/pdf)
- [Bolton et al. (2012) – AJ, 144, 5](https://iopscience.iop.org/article/10.1086/668105/pdf)

---

## Technical Implementation Notes

### Rest-Frame Reconstruction

All spectral reconstructions are performed in the **rest frame** to enable consistent comparison across different redshifts.

### Redshift Range Selection

To avoid spectral regions with poor sampling or missing information, a restricted rest-frame redshift range is adopted:

> **Adopted range:** `z > 2` for the PCA reconstruction

**Rationale:**
- Ensures adequate spectral coverage across the full wavelength range
- Avoids low signal-to-noise regions
- Enables physically meaningful template construction for high-redshift quasars

### Data Sources

- **Survey:** DESI Data Release 1 (DR1) & DR2
- **Object type:** Main-survey quasars (QSOs)
- **Low-z range:** `0.5 ≤ z ≤ 1.0`
- **High-z range:** `2.0 ≤ z ≤ 4.0`

---

## Dependencies

- DESI data access tools (SPARCL client)
- scikit-learn (PCA implementation)
- astropy, numpy, matplotlib
- astroML (reference implementations)

---

## Usage

1. Run `desi_spectra_prep.ipynb` to retrieve and prepare spectra
2. Execute `desi_pca.ipynb` to perform PCA fitting and generate templates
3. Consult `DESI_access_spectra.ipynb` for data loading examples

---

## Outputs

- **Spectral templates:** PCA components in rest frame for z > 2 quasars
- **Visualizations:** Comparison plots between low-z and high-z populations
- **Decomposition file:** `spec_decompositions.pkl` for downstream applications