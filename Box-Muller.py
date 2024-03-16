#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt

def box_muller(size):
    """
    Generates standard normal random variables using the Box-Muller algorithm.

    Args:
        size: The desired number of random samples.

    Returns:
        A NumPy array of standard normal random variables.
    """

    num_pairs = np.ceil(size / 2).astype(int)  # Number of pairs to generate

    R = np.sqrt(-2 * np.log(np.random.rand(num_pairs)))
    theta = 2 * np.pi * np.random.rand(num_pairs)

    X = R * np.cos(theta)
    Y = R * np.sin(theta)

    samples = np.concatenate((X, Y))[:size]  # Combine and truncate to size
    return samples

# **Testing**
samples = box_muller(10001)

print("length(samples): ", len(samples))  # Check the number of samples

# **Visualizing the Distribution**
plt.hist(samples, density=True, bins=50)  # Histogram with density normalization
xs = np.linspace(min(samples), max(samples), 200)
ys = np.exp(-xs**2 / 2) / np.sqrt(2 * np.pi)  # Theoretical normal density
plt.plot(xs, ys, color='red')
plt.title("Box-Muller Generated Samples vs. Standard Normal")
plt.show()

# **Kolmogorov-Smirnov Test (You may need to install SciPy)**
from scipy.stats import kstest, norm

result = kstest(samples, norm.cdf)
print(result)

