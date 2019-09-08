#! /usr/bin/python


def read_file(filename):
    try:
        with open(filename) as f_obj:
            content = f_obj.read()
    except FileNotFoundError:
        print("the file you are opening is not exist.")
    else:
        print(content)


filenames = ['cats.txt', 'dogs.txt', 'ppp.txt']
for file in filenames:
    read_file(file)
