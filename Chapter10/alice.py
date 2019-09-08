#! /usr/bin/python

filename = 'alice.txt'

try:
    with open(filename) as obj_fn:
        content=obj_fn.read()
except FileNotFoundError:
    print("This file is not exist.")
else:
    print(content)

