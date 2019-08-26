#!/usr/bin/python

users={
    'first_name':'li',
    'last_name':'Wang',
    'age':37,
    'city':'Beijing',
}

for key,value in users.items():
    print("\n"+key.title()+":"+str(value).title())
