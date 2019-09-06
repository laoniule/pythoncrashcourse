#!/usr/bin/python

from random import randint
# x=randint(1,6)
# print(x)

class Die():
    def __init__(self,sides=6):
        self.sides=sides
        # self.x =randint(1,sides)
        # print(self.x)

    def roll_die(self):
        self.side=randint(1,self.sides)
        print(self.side)

die1=Die(10)

for i in range(0,10):
    die1.roll_die()


