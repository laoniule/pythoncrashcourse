#!/usr/bin/python


def make_great(magicians):
    for i in range(0, len(magicians)):
        magicians[i] = " the Great "+magicians[i]


def show_magicians(magicians):
    for magician in magicians:
        print(magician)


magicians = ["a", "b", "c", "d"]
copy_magicians=magicians[:]
#make_great(magicians)
make_great(copy_magicians)
show_magicians(magicians)
show_magicians(copy_magicians)
