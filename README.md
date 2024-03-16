# Project: Random Variable Simulation with Transformation Methods

This project demonstrates the implementation of common transformation methods for generating random variables from various probability distributions.  It includes the following core algorithms:

* **Box-Muller Algorithm:** Transforms uniform random variables into standard normal random variables, providing a foundation for simulating normally distributed data.
* **Exponential to Gamma Transformation:**  Demonstrates how summing independent exponentially distributed random variables and applying a scaling factor can generate random variables following the Gamma distribution.
* **Multivariate Normal Simulation:**  Employs the Cholesky decomposition to transform standard normal random variables into correlated normal random variables following a multivariate normal distribution. 

## Code Examples

* **`box_muller.py`:**  Implementation of the Box-Muller algorithm for standard normal random variable generation, along with visualization and a Kolmogorov-Smirnov test for verification.
* **`Transformation Gamma.py`:** Simulates Gamma-distributed random variables by transforming exponential random variables. Includes calculations to verify the generated distribution's mean and standard deviation.
* **`MVNwith_cholesky_factorization.py`:** Demonstrates the generation of multivariate normal random variables.  Includes visualization of the simulated data and estimation of the mean and covariance.

## Summary

Transformation methods provide a powerful and computationally efficient approach for simulating random variables from complex probability distributions. These techniques leverage known distributions and mathematical transformations to generate values from desired target distributions.  

## How to Run the Examples

1. **Prerequisites:** 
   * Python 3+
   * NumPy
   * Matplotlib
   * SciPy (for statistical tests)

2. **Running the Code:**
   * From your terminal, navigate to the project directory. 
   * Execute the Python files. For example: `box_muller.py`

<p align="center">
![mvn_samples](https://github.com/andrewrobson3000/Transformation-Methods-for-Statistical-Modeling-and-Simulation/assets/87878168/c9725d05-d926-4cf1-bcfa-fddd25424fdb)
</p>
