# planck_model.py — data, theory and likelihood for the Planck TT MCMC.
# Packaged as a module so worker processes can import it under the 'spawn'
# start method (required on macOS; avoids the OpenMP + fork deadlock).
import os
# single-threaded per process — set BEFORE importing numpy/camb in every worker
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS",
           "VECLIB_MAXIMUM_THREADS"):
    os.environ[_v] = "1"
import urllib.request
import numpy as np
import camb

# ---- data: Planck 2018 binned TT (downloaded once, cached) ----
DATA_DIR = "data"
FNAME = "COM_PowerSpect_CMB-TT-binned_R3.01.txt"
URL = ("https://irsa.ipac.caltech.edu/data/Planck/release_3/"
       "ancillary-data/cosmoparams/" + FNAME)
os.makedirs(DATA_DIR, exist_ok=True)
_path = os.path.join(DATA_DIR, FNAME)
if not os.path.exists(_path):
    urllib.request.urlretrieve(URL, _path)
ell, Dl, _lo, _hi, _bf = np.loadtxt(_path, unpack=True)   # l, Dl, -dDl, +dDl, BestFit
err = 0.5 * (_lo + _hi)                                   # symmetric per-bin error

# ---- theoretical binned D_l^TT with CAMB ----
LMAX = int(np.ceil(ell.max())) + 50

def theory_dl(theta):
    """Binned theory D_l^TT [muK^2] at the data multipoles.
    theta = [ombh2, omch2, H0, tau, ln10As, ns]."""
    ombh2, omch2, H0, tau, ln10As, ns = theta
    pars = camb.set_params(H0=H0, ombh2=ombh2, omch2=omch2, tau=tau,
                           As=1e-10 * np.exp(ln10As), ns=ns,
                           mnu=0.0, lmax=LMAX, lens_potential_accuracy=0)
    res = camb.get_results(pars)
    dl = res.get_cmb_power_spectra(pars, CMB_unit="muK")["total"][:, 0]
    return np.interp(ell, np.arange(dl.size), dl)

# ---- priors, likelihood, posterior ----
theta_fid = np.array([0.02237, 0.1200, 67.36, 0.0544, 3.044, 0.9649])
BOUNDS = np.array([[0.018, 0.026], [0.10, 0.14], [55.0, 80.0],
                   [0.01, 0.12], [2.7, 3.3], [0.92, 1.00]])
TAU_MU, TAU_SIG = 0.0544, 0.0073
NDIM = BOUNDS.shape[0]

def log_prior(theta):
    if np.any(theta < BOUNDS[:, 0]) or np.any(theta > BOUNDS[:, 1]):
        return -np.inf
    return -0.5 * ((theta[3] - TAU_MU) / TAU_SIG) ** 2

def log_likelihood(theta):
    try:
        model = theory_dl(theta)
    except Exception:
        return -np.inf
    return -0.5 * np.sum(((Dl - model) / err) ** 2)

def log_posterior(theta):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(theta)
