#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   word_population.py
@Time    :   2019/09/19 17:31:13
@Author  :   Niu Xiaodong
@Version :   1.0
@Contact :   xniu@msn.com
@License :   (C)Copyright 2017-2018
@Desc    :   None
'''

# here put the import lib

import json

filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

    for pop_dict in pop_data:
        if pop_dict["Year"] == '2000':
            country_name = pop_dict["Country Name"]
            population = pop_dict["Value"]
            print(country_name + ":" + population)
