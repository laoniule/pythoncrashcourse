#!/usr/bin/python

import json

numbers = [2, 5, 6, 3, 9, 7]

filename = 'numbers.json'
with open(filename, 'w') as f_obj:
    json.dump(numbers, f_obj)
