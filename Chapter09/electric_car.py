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



class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
            
        self.battery_size = 70

    def describe_battery(self):
        print("This car has a " + str(self.battery_size)+"-kwh battery")

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
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
