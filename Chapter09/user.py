class User():
    def __init__(self,firstname,lastname,sex,age):
        self.firstname=firstname
        self.lastname=lastname
        self.sex=sex
        self.age=age
        self.fullname=self.firstname+" "+self.lastname


    def describe_user(self):
        print("User Info: ")
     
        print("Username: "+self.fullname+"\tSex: "+self.sex \
            + "\tAge: "+str(self.age))

    def greet_user(self,greet):
        print(greet + self.fullname)

user1=User("wang","li","woman",35)
user1.greet_user("Hello ")
user1.describe_user()
