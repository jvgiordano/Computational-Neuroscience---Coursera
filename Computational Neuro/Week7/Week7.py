#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 17:10:24 2017

@author: jonny
"""

import numpy as np

Q = np.matrix('0.15 0.1; 0.1 0.12')
print(Q)

eigen_val, eigen_vec = np.linalg.eig(Q)

print("eigen values:")
print(eigen_val)
print("eigen vector")
print(eigen_vec)
print("eigen vectors doubled")
print(eigen_vec*2)