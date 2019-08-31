#!/usr/bin/python


def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = str(first)
    profile['last_name'] = str(last)
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile(
    "albert", "einstein", location="princeton", field="physics")
print(user_profile)
