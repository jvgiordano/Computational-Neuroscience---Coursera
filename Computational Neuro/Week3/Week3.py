#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 11:36:42 2017

@author: jonny
"""

from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

sigma_1 = 0.5
mew_1 = 5
s_1 = np.random.normal(mew_1,sigma_1,1000)
count_1,bins_1, ignored_1 = plt.hist(s_1, 301, normed=True)
s1_plot = plt.plot(bins_1, 1/(sigma_1 * np.sqrt(2 * np.pi)) * np.exp( - (bins_1 - mew_1)**2 / (2 * sigma_1**2) ), linewidth=2, color='r')

sigma_2 = 1
mew_2 = 7
s_2 = np.random.normal(mew_2,sigma_2,1000)
count_2,bins_2, ignored_2 = plt.hist(s_2, 301, normed=True)
s2_plot = plt.plot(bins_2, 1/(sigma_2 * np.sqrt(2 * np.pi)) * np.exp( - (bins_2 - mew_2)**2 / (2 * sigma_2**2) ), linewidth=2, color='r')


plt.plot(s1_plot,s2_plot,'r')
plt.show()
