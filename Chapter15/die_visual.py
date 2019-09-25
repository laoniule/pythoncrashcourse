#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   die_visual.py
@Time    :   2019/09/22 11:54:48
@Author  :   Niu Xiaodong 
@Version :   1.0
@Contact :   xniu@msn.com
@License :   (C)Copyright 2017-2018
@Desc    :   None
'''

# here put the import lib
import pygal
from die import Die

die1 = Die()
die2 = Die()

results = []
for roll_num in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)

#print(results)

frequencies = []
max_results = die1.num_sides + die2.num_sides
for value in range(2, max_results + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

hist = pygal.Bar()

hist.title = "Results of rolling one D6"
#hist.x_labels = ["2", "3", "4", "5", "6","7","8","9","10","11","12"]
hist.x_labels=map(str,range(2,13))
hist.x_title = "Result"
hist.y_title = "Frequncy of result"

hist.add('D6', frequencies)
hist.render_to_file("die_visual2.svg")