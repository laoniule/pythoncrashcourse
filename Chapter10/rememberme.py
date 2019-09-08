#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   rememberme.py
@Time    :   2019/09/08 11:00:14
@Author  :   Niu Xiaodong 
@Version :   1.0
@Contact :   xniu@msn.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
import json


def greet_user():
    filename = 'username.json'

    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        username = input("Input your name?")
        with open(filename, 'w') as f_obj:
            json.dump(username, f_obj)
            print("We will remember you when you come back " + username+".")
    else:
        print("Welcome back " + username)


greet_user()
