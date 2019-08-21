import os

print(os.getcwd())

filename = os.getcwd() + "\\Chapter10\\pi_digits.txt"

with  open(filename) as file_object:
    contents = file_object.read()
    print(contents)
