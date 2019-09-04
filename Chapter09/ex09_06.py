#! /usr/bin/python


class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)
        print("customer number served is " + str(self.number_served))

    def set_number_served(self):
        self.number_served = 5

    def increase_number_served(self):
        self.number_served += 1

    def open_restaurant(self):
        print("restaurant is opening!")


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocalate', 'durian']

    def print_flavors(self):
        print("\n")
        for flavor in  self.flavors:
            print(flavor)


# my_restaurant = Restaurant("牛小馆", "肥牛火锅")
# my_restaurant.describe_restaurant()
# my_restaurant.open_restaurant()

# my_restaurant.set_number_served()
# my_restaurant.describe_restaurant()

# my_restaurant.increase_number_served()
# my_restaurant.describe_restaurant()

myFavoritesIceCream = IceCreamStand('麦当劳甜品', '冰激凌')
myFavoritesIceCream.print_flavors()