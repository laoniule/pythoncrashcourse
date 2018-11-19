class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reader=0

    def get_description_name(self):
        long_name=self.make+ " " +self.model+" "+str(self.year)
        return long_name


    def read_odometer(self):
        print("This car has run "+str(self.odometer_reader)+" mile{s}.")

    def update_odometer(self,newmile):
        if newmile>self.odometer_reader:
            self.odometer_reader=newmile
        else:
            print("You can rollback an odometer.")


newcar=Car("Audi","A4",2016)
print(newcar.get_description_name())
newcar.update_odometer(30)
newcar.read_odometer()
newcar.update_odometer(5)
newcar.read_odometer()