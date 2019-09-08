#!/usr/bin/python

import json


# numbers = [2, 5, 6, 3, 9, 7]

filename = 'numbers.json'

with open(filename ) as f_obj:
    numbers=json.load(f_obj)
    print(numbers)
