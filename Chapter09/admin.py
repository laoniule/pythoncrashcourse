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


class Priviledges():
    def __init__(self):
        self.privileges=["can add post","can delete post","can ban user"]


    def show_privileges(self):
 #       print("{} ,You have privileges below: ".format(self.fullname))
        for v in self.privileges:
            print(v)

class Admin(User):
    def __init__(self,firstname,lastname,sex,age):
        super().__init__(firstname,lastname,sex,age)
        self.fullname=self.firstname+self.lastname
        
        self.priviledges=Priviledges()
        




user1=User("wang","li","woman",35)
user1.greet_user("Hello ")
user1.describe_user()
 
user2=User("Niu","Xiaodong","Man",48)
user2.greet_user("How are you，")

admin=Admin("zhang","Yun","man",26)
admin.priviledges.show_privileges()