#!/usr/bin/python


class User():

    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.login_times = 0

    def describe_user(self):
        print("FirstName: "+self.first_name)
        print("LastName: "+self.last_name)
        print("Gender: " + self.gender)
    #    print("you have try ti login " + str(self.login_times)+" times.")

    def increment_login_times(self):
        self.login_times += 1

    def reset_login_times(self):
        self.login_times = 0

    def greet_user(self):
        print("You are welcome!" + self.first_name + " " + self.last_name)
        print("you have try ti login " + str(self.login_times)+" times.")


class Admin(User):
    def __init__(self, first_name, last_name, gender):
        super().__init__(first_name, last_name, gender)

        self.privileges=["CAn add post","can delete post","can ban user"]

    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

# niu = User("Niu", "xd", "man")
# niu.describe_user()
# niu.greet_user()

# for i in range(1, 4):
#     niu.increment_login_times()
#     niu.greet_user()


# niu.reset_login_times()
# niu.greet_user()

njx=Admin("Niu","JX","lady")

njx.show_privileges()