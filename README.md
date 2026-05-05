# advanced_lab
Learning scripts, notebooks, and notes for the course Advanced Data Lab taken in the University of Guanajuato under the supervision of Prof. Alma González.

### Topic 1: Metropolis Algorithm
In the notebook metropolis_full.ipynb, I implement the bayesian inference metropolis algorithm on two data sets of linear functions: data-1.dat and line-2.dat, produced with the equation y = -0.91x + 4.00.

In the plot of Section 6, we find that the major differences between the two datasets is their dispersion and single data errors. The line-1.dat data follows the line equation closely, meanwhile the line-2.dat data shows greater dispersion and erros that do not seem to correspond to that deviation from the line. It tells us that for the second case we must use a nuisance parameter f in the single data errors evaluated in the log-posterior minimization process. In particular, sigma_eff^2 = sigma_i^2 + f^2 (mx + b)^2, where f becomes an extra parameter that characterizes the hidden errors that are not being accounted. Both models, with and without the nuisance parameter are evaluated.

The notebook is structured as follows:
1. Load the data
2. Define the log-posterior models with and w/o the nuisance parameter f as functions.
3. Define the metropolis algorithm and walkers functions.
4. Run the inference procedure with model A (with f).
5. Run the inference procedure with model B (w/o f).
6. Plot the data fitted lines in both models A and B.
7. Plot the path followed by the walkers (four) until reaching the minimization values. The gray lines are the burn-in steps that are not considered when taking the median values.
8. Corner plots; marginal posteriors showing the median values of the two datasets parameters infered with models A and B. 
9. Summary.

### Findings:
- The line-1.dat shows a almost perfect correspondence to the true line equation: y = -0.91x + 4.00. Including a nuisance parameter is not necessary.
- The line-2.dat shows high dispersion of the data compared to the line equation. Also, it is important to note that the errors reported in the data are also dispersed and do not seem to correspond to the true errors for the data. It is evident the necessity of the use of a model that incorporates a nuisance parameter f. It is also evident in the deviation of the abcisa cut found with the model A: b=4.99, when the true value is b=4.00.
- The paths followed by the walkers in the model A are straightforward. Even when we saw that the result for b is not correct. Meanwhile, when the model B is used, the paths are now converging to the same regions. For the walker three (green), there is a convergence region reached, far from the true parameter values. At the end, the average of the walkers gives a final result that coincides with the true values with good accuracy.
- It is also evident in the triangle plots. The results for the model B show two regions but the walkers prefer the region that finally give a good result. The question would be, how can I be confident of a result when there are two regions?