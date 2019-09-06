#!/usr/bin/bash

prompt = "Please enter your age: "
prompt += "\n input 'quit' to exit "

active = True
while active:
    age = input(prompt)
    if age != "quit":
        age = int(age)
        if age < 3:
            print("ticket is free")
        elif age >= 3 and age < 12:
            print("should pay $10")
        elif age >= 12:
            print("should pay $15")
    else:
        active = False
