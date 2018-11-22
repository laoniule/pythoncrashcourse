class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reader = 0

    def get_description_name(self):
        long_name = self.make + " " + self.model+" "+str(self.year)
        return long_name

    def read_odometer(self):
        print("This car has run "+str(self.odometer_reader)+" mile{s}.")

    def update_odometer(self, newmile):
        if newmile > self.odometer_reader:
            self.odometer_reader = newmile
        else:
            print("You can rollback an odometer.")

    def fill_gas_tank(self):
        print("This car has a 55L gas tank")



class Battery():
    def __init__(self,battery_size=70):
        self.battery_size=battery_size

    def upgrade_battery(self):
        if self.battery_size!=85:
            self.battery_size=85


    def get_range(self):
        """打印一条消息，指出电瓶的续航里程"""
        if self.battery_size==70:
            range=240
        elif self.battery_size==85:
            range=270

        message="This car can go approximately "+str(range)
        message+=" miles on a full charge."

        print(message)

    def describe_battery(self):
        print("This car has a " + str(self.battery_size)+"-kwh battery.")

    
        

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)     
        
        self.battery=Battery()
    
  

    def fill_gas_tank(self):
        print("This eletric car doesn't need a gas tank!")


newcar = Car("Audi", "A4", 2016)
print(newcar.get_description_name())
newcar.update_odometer(30)
newcar.read_odometer()
newcar.update_odometer(5)
newcar.read_odometer()
newcar.fill_gas_tank()


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_description_name())
my_tesla.read_odometer()
my_tesla.update_odometer(100)
my_tesla.read_odometer()

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("\n升级电池容量")

my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()