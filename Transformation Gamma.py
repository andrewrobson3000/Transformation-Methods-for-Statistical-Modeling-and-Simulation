#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

# Simulate X~Gamma(a, b)
n = 10000
a = 7
b = 0.5

# Generate exponential random variables
U = np.random.exponential(scale=1, size=(a, n))

# Sum and scale to simulate Gamma(a, b) variables
X = U.sum(axis=0) / b

# Check
mean_X = np.mean(X)
std_X = np.std(X) / np.sqrt(n)

print(f"Mean of X: {mean_X}, should be approximately {a/b}")
print(f"Standard deviation of X: {std_X}, should be approximately {np.sqrt(a/n)/b}")


# In[ ]:




