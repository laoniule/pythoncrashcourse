class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.open_time = 9
        self.number_served=0

    def description_restaurant(self):
        print("\nThe restaurant's name is "+self.restaurant_name)
        print("cuisine type is "+self.cuisine_type)

    def open_restaurant(self):
        print("The restaurant open at "+str(self.open_time)+" o'clock AM")

    def reserved_number(self):
        print("The restaurant has reserved "+str(self.number_served)+" people{s}")


    def set_number_serverd(self, number):
        self.number_served=number
        
    def incredment_number_served(self,plan_number):
        while self.number_served<plan_number:
            self.number_served+=1
            self.reserved_number()

# myrestaurant = Restaurant("xiaoguan", "pengtiao")
# myrestaurant.description_restaurant()
# myrestaurant.open_restaurant()
# myrestaurant.reserved_number()

# hisrestaurant = Restaurant("maidanglao", "hanbao")
# hisrestaurant.description_restaurant()
# hisrestaurant.reserved_number()
# hisrestaurant.set_number_serverd(30)
# hisrestaurant.incredment_number_served(80)
# hisrestaurant.reserved_number()
