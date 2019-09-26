#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   mpl_squares.py
@Time    :   2019/09/08 16:59:03
@Author  :   Niu Xiaodong
@Version :   1.0
@Contact :   xniu@msn.com
@License :   (C)Copyright 2017-2018
@Desc    :   None
'''

# here put the import lib

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5, 6]
squares = [1, 4, 9, 16, 25, 36]
plt.plot(input_values, squares, linewidth=5)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square Value", fontsize=14)
plt.tick_params(axis="both", labelsize=14)
plt.show()