#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   ex15_01.py
@Time    :   2019/09/09 10:58:10
@Author  :   Niu Xiaodong 
@Version :   1.0
@Contact :   xniu@msn.com
@License :   (C)Copyright 2017-2018
@Desc    :   None
'''

# here put the import lib
import matplotlib.pyplot as plt

x_values = list(range(1, 500))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Greens, s=20)
plt.title("Cube Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)
plt.tick_params(axis="both", labelsize=14)
plt.show()
