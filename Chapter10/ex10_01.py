#!/usr/bin/python

import os

filename = os.path.abspath(os.path.dirname(__file__)) + '\\learning_python.txt'

with open(filename) as file_object:
    # content = file_object.read()
    # print(content)
    lines = file_object.readlines()

for line in lines:
    print(line.strip())
