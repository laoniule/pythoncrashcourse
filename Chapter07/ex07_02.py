#!/usr/bin/python

prompt = input("how many people are coming? ")
prompt = int(prompt)

if prompt > 8:
    print("no table availabel")
else:
    print("ok,table for "+str(prompt))