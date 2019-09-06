#!/usr/bin/python
import os

propmpt_text = "What's your name?"

filename = os.getcwd() + "\\guest.txt"

with open(filename,'w') as obj_file:
    prompt = input(propmpt_text)
    obj_file.write(prompt)


