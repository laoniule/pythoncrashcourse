#! /usr/bin/python

#filename = 'alice.txt'

def word_count(filename):
    try:
        with open(filename) as obj_fn:
            content=obj_fn.read()
    except FileNotFoundError:
        print("This file is not exist.")
    else:
        words=content.split()
        counts=len(words)
        print("the file include "+ str(counts) + " words.")
  

filename = 'alice.txt'
word_count(filename)