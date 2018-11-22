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
        """读里程表"""
        print('This car has run {} miles.'.format(str(self.odometer_reader)))

    def update_odometer(self, newmile):
        """设置里程表为指定的值，拒绝里程表往回拨"""
        if newmile > self.odometer_reader:
            self.odometer_reader = newmile
        else:
            print("You can rollback an odometer.")


    def increase_odometer(self,miles):
        """将里程表读数增加指代的量"""
        self.odometer_reader+=miles

    def fill_gas_tank(self):
        print("This car has a 55L gas tank")

""" newcar = Car("Audi", "A4", 2016)
print(newcar.get_description_name())
newcar.update_odometer(30)
newcar.read_odometer()
newcar.update_odometer(5)
newcar.read_odometer()
 """