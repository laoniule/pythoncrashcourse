import os

print(os.getcwd())

filename = os.getcwd() + "\\pi_digits.txt"

with  open(filename) as file_object:
    # contents = file_object.read()
    # print(contents.rstrip())
    for line in file_object:
        print(line.rstrip())