#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   greet_user.py
@Time    :   2019/09/08 11:09:44
@Author  :   Niu Xiaodong 
@Version :   1.0
@Contact :   xniu@msn.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
import json


def get_stored_username():
    filename = 'username.json'

    try:
        with open(filename) as f_obj:
            username = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("What's your name?")
    filename = 'username.json'
    with open(filename, 'w') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back "+username+"!")
    else:
        username = get_new_username()
        print("We'll remember you " + username)


greet_user()
