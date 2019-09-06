#!/usr/bin/python
import os

propmpt_text = "What's your name?"

filename = os.getcwd() + "\\guest_book.txt"

print("input 'q' to exit")
while True:
    with open(filename,'a') as obj_file:
        prompt = input(propmpt_text)
        
        if prompt=="q":
            break
        else:
            obj_file.write(prompt+"\n")


