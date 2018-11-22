from car import Car

my_new_car=Car("Audi","A4",2016)
print(my_new_car.get_description_name())
my_new_car.odometer_reader=23
my_new_car.read_odometer()