#!/usr/bin/python

def  describe_city(city,country="China"):
    print(city.title()+" is in "+country.title()+".")

describe_city("shanghai","China")
describe_city("Beijing")
describe_city("tokyo","japan")