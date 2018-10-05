#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 10:47:05 2017

@author: jonny
"""

import pickle
import math
import numpy as np
import matplotlib.pyplot as plt

with open('tuning_3.4.pickle', 'rb') as f:
    data = pickle.load(f)
    
with open('pop_coding_3.4.pickle', 'rb') as f:
    data_2 = pickle.load(f)

avg_neuron1 = np.mean(data["neuron1"], axis=0)
print (avg_neuron1[0])
avg_neuron2 = np.mean(data["neuron2"], axis=0)
avg_neuron3 = np.mean(data["neuron3"], axis=0)
avg_neuron4 = np.mean(data["neuron4"], axis=0)


plt.figure(1)
plt.plot(data["stim"], avg_neuron1)
plt.figure(2)
plt.plot(data["stim"], avg_neuron2)
plt.figure(3)
plt.plot(data["stim"], avg_neuron3)
plt.figure(4)
plt.plot(data["stim"], avg_neuron4)

#Find R_MAX1 Find and Plot
r_max1 = max(avg_neuron1)
r_max1_index = np.where(avg_neuron1==r_max1)
plt.figure(1)
plt.plot(data["stim"][r_max1_index],r_max1,'ro')

#Find R_MAX2 Find and Plot
r_max2 = max(avg_neuron2)
r_max2_index = np.where(avg_neuron2==r_max2)
plt.figure(2)
plt.plot(data["stim"][r_max2_index],r_max2,'ro')

#Find R_MAX2 Find and Plot
r_max3 = max(avg_neuron3)
r_max3_index = np.where(avg_neuron3==r_max3)
plt.figure(3)
plt.plot(data["stim"][r_max3_index],r_max3,'ro')

#Find R_MAX3 Find and Plot
r_max4 = max(avg_neuron4)
r_max4_index = np.where(avg_neuron4==r_max4)
plt.figure(4)
plt.plot(data["stim"][r_max4_index],r_max4,'ro')

#Sum 10 trials for R1
r1 = sum(data_2["r1"])
r2 = sum(data_2["r2"])
r3 = sum(data_2["r3"])
r4 = sum(data_2["r4"])

#Normalize 10 Trials for R1
r1 = r1/r_max1
r2 = r2/r_max2
r3 = r3/r_max3
r4 = r4/r_max4

#Multiply by basis vectors
r1 = r1 * data_2["c1"]
print ("r1")
print (r1)

r2 = r2 * data_2["c2"]
print ("r2")
print (r2)

r3 = r3 * data_2["c3"]
print ("r3")
print (r3)

r4 = r4 * data_2["c4"]
print ("r4")
print (r4)

v_pop = r1+r2+r3+r4
print("v_pop")
print(v_pop)

angle = 90 - math.cos(v_pop[0]/v_pop[1])*(180/(2*3.14))
print("angle")
print(angle)
