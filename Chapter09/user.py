class User():
    def __init__(self, firstname, lastname, sex, age):
        self.firstname = firstname
        self.lastname = lastname
        self.sex = sex
        self.age = age
        self.fullname = self.firstname+" "+self.lastname
        self.login_attempts = 0

    def describe_user(self):
        print("User Info: \n")
        print("Username: "+self.fullname+"\tSex: " + self.sex + 
            "\tAge: "+str(self.age))

    def greet_user(self, greet):
        print(greet + self.fullname)


    def reset_login_attempts(self):
        self.login_attempts = 0


    def increment_login_attempts(self):
        if self.login_attempts<3:
            print("login")
            self.login_attempts+=1
            
        else:
            print('You have got 3 times to attemp to login.reset to 0')
            self.reset_login_attempts()




user1 = User("wang", "li", "woman", 35)
user1.greet_user("Hello ")
user1.describe_user()
user1.increment_login_attempts()


user2 = User("Niu", "Xiaodong", "Man", 48)
user2.greet_user("How are you，")
user2.describe_user()
