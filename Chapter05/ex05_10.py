#!/usr/bin/python
current_users=["Rousseau","Freud","Heidegger","Schopenhauer","Max"]
new_users=["rousseau","Freud","Leibniz","Max","lionerd"]

current_users_lowers=[_user.lower() for _user in current_users ]

for user in new_users:
    if user.lower() in current_users_lowers:
        print("user account " ,user, " is exists,please input another user name")
    else:
        print("you can register ther user account",user)
