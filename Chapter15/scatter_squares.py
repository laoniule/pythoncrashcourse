#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   scatter_squares.py
@Time    :   2019/09/09 10:33:10
@Author  :   Niu Xiaodong 
@Version :   1.0
@Contact :   xniu@msn.com
@License :   (C)Copyright 2017-2018
@Desc    :   None
'''

# here put the import lib
import matplotlib.pyplot as plt

# x_value=[1,2,3,4,5]
# y_value=[1,4,9,16,25]

x_value = list(range(1, 1001))
y_value = [x**2 for x in x_value]

plt.scatter(x_value,
            y_value,
            c=y_value,
            cmap=plt.cm.Blues,
            edgecolor="none",
            s=4)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.axis([0, 1100, 0, 1100000])

plt.tick_params(axis="both", which="major", labelsize=14)
plt.show()
# plt.savefig('squares_plot.png', bbox_inches='tight')
