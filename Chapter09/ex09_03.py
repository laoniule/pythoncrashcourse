#!/usr/bin/python


class User():

    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender

    def describe_user(self):
        print("FirstName: "+self.first_name)
        print("LastName: "+self.last_name)
        print("Gender: " + self.gender)

    def greet_user(self):
        print("You are welcome!" + self.first_name + " " + self.last_name)


niu = User("Niu","xd","man")
niu.describe_user()
niu.greet_user()