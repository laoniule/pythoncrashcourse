#! /usr/bin/python


def read_file(filename):
    try:
        with open(filename) as f_obj:
            content = f_obj.read()
    except FileNotFoundError:
        pass
    else:
        print(content)


filenames = ['cats.txt', 'dogs.txt', 'ppp.txt']
for file in filenames:
    read_file(file)
