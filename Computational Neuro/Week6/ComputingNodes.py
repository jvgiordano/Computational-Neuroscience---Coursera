#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 18:32:15 2017

@author: jonny
"""
import numpy as np


# Create Matrix W
W = np.zeros((5,5))

for i in range(5):
    for j in range (5):
        if i != j:
            W[i][j] = 0.1
        else:
            W[i][j] = 0.6

print("Matrix W")
print(W)

#Create Matrix u

u = [[0.6],[0.5],[0.6],[0.2],[0.1]]
print("Matrix u")
print(u)

# Create Matrix M
M = np.zeros((5,5))

for i in range(5):
    for j in range (5):
        if i == j:
            M[i][j] = -0.5
        elif (i == j+1) or ( i == j-1) or (i == j+4) or (i == j-4):
            M[i][j] = 0
        else:
            M[i][j] = 0.5
             
                 
print("Matrix M")
print(M)


h = np.dot(W,u)
print ("Matrix h:")
print (h)

eigen_val, eigen_vec = np.linalg.eigh(M)
print ("Eigen vector")
print (eigen_vec)
print ("Eignen value")
print (eigen_val)

temp = np.ones((5,1))

z = 1
for x in range(5):
    z *= (1-eigen_val[x])
    
V


             
             
             
             
             
             
             