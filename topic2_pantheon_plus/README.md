### Topic 1: Metropolis Algorithm

In the notebook

The notebook is structured as follows:

1. 

### Findings

- When using the nuisance parameter for the line-1.dat data the system pushes logf -> -inf, which gives doesn't allow the walker to explore correctly the parameter space. The solution is to reset the position of logf inside the prior interval. This effect is due to the almost perfect agreement of data to the model indicating that for this problem there's is no need of this nuisance parameter.
