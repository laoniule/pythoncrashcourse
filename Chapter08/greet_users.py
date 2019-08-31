#! /usr/bin/python

def greet_users(names):
    for name in names:
        msg="Hello, " + name.title() +"!"
        print(msg) 


usernames=['hanah','ty','margot']
greet_users(usernames)
