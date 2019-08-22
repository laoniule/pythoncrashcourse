#!/usr/bin/python

#users=["wl","njx","ww","cz","admin"]
users=[]
if users:
    for user in users:
        if user.lower()=="admin":
            print(user,",would you like print a status report")
        else:
            print("Hello ",user.title(),",You are welcome to login")
else:
    print("We need some users")