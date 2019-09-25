#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   rw_visual.py
@Time    :   2019/09/20 22:07:43
@Author  :   Niu Xiaodong
@Version :   1.0
@Contact :   xniu@msn.com
@License :   (C)Copyright 2017-2018
@Desc    :   None
'''

# here put the import lib

import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_walk = input("run another walk?(Y/N)")
    if keep_walk == "n":
        break
