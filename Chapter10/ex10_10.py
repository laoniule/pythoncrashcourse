#!/usr/bin/python


def word_count(filename):
    try:
        with open(filename) as f_obj:
            lines = f_obj.readlines()
    except FileNotFoundError:
        print("file is not exist.")
    else:
        for line in lines:
            wordnum = line.count("are")
            print(wordnum)


filename = 'atextfile.txt'
word_count(filename)
