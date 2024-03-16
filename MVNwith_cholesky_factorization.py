#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

# Given mean vector mu and covariance matrix S
mu = np.array([-1, 1])
S = np.array([[5, -3], [-3, 4]])

# Cholesky decomposition of the covariance matrix
L = np.linalg.cholesky(S)

# Number of samples to generate
n = 10000

# Generate n sets of standard normal random variables
Z = np.random.normal(size=(2, n))

# Transform Z into the MVN distribution with mean mu and covariance S
X = L @ Z + mu[:, np.newaxis]

# Plot the generated MVN samples
plt.figure(figsize=(10, 6))
plt.scatter(X[0, :], X[1, :], alpha=0.2)
plt.axis('equal')
plt.title('Samples from a Multivariate Normal Distribution')
plt.xlabel('$X_1$')
plt.ylabel('$X_2$')
plt.grid(True)
plt.show()

# Estimate the mean and covariance of the generated samples
estimated_mean = np.mean(X, axis=1)
estimated_covariance = np.cov(X)

print(f"Estimated Mean: {estimated_mean}")
print(f"Estimated Covariance: \n{estimated_covariance}")

