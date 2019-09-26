#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   highsandlows.py
@Time    :   2019/09/19 10:38:22
@Author  :   Niu Xiaodong
@Version :   1.0
@Contact :   xniu@msn.com
@License :   (C)Copyright 2017-2018
@Desc    :   None
'''

# here put the import lib

import csv
import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt

filename = 'sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    #    print(reader)
    header_row = next(reader)
    #print(header_row)

    # for index,column_header in enumerate(header_row):
    #     print(index,column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], "%Y/%m/%d")
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            print(current_date,"Missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
        


    #print(highs)

    #a=[9,3,7,6,8,10]
    fig = plt.figure(dpi=128, figsize=(10, 6))

    plt.plot(dates, highs, c="red", alpha=0.5)
    plt.plot(dates, lows, c="blue", alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)
    plt.title("Daily Highest Tempreture", fontsize=24)
    plt.xlabel("", fontsize=16)
    plt.ylabel("temperature", fontsize=12)
    plt.tick_params(axis="both", which="major", labelsize=20)
    plt.yticks(np.arange(0,101,10))
    plt.show()