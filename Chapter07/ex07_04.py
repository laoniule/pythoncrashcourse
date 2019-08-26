#!/usr/bin/python

prompt = "What would you like to add in pizza? "

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print("add some " + message)