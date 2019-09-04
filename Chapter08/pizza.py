#!/usr/bin/python


def make_pizza(size, *toppings):
    print("\nMaking a " + str(size) + " inches pizza with the following \
topings:")
    for topping in toppings:
        print("-" + topping)


# make_pizza(16, 'peperoni')
# make_pizza(12, 'mushroom', 'great peppers', 'extra cheease')
