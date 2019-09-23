#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   die.py
@Time    :   2019/09/22 11:50:23
@Author  :   Niu Xiaodong 
@Version :   1.0
@Contact :   xniu@msn.com
@License :   (C)Copyright 2017-2018
@Desc    :   None
'''

# here put the import lib
from random import randint

class Die():

    def __init__(self,num_sides=6):
        self.num_sides=num_sides

    def roll(self):
        return randint(1,self.num_sides)
    
       