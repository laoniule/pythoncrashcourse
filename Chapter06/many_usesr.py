#!/usr/bin/python

users = {
    'aeinstein': {
        'firstname':'albert',
        'lastname':'einstein',
        'location':'priceton',
    },

    'mcurie': {
        'firstname':'marie',
        'lastname':'curie',
        'location':'paris',                
    }
}

for username,user_infor in users.items():
    print("\nUsername: " + username)
    full_name = user_infor['firstname']+ ' '+user_infor['lastname']
    location = user_infor['location']
    print("\tFull name: " + full_name.title())
    print("\tLocation: "+ location.title())
