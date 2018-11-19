# 任意数量参数的使用

def make_pizza(size,*toppings):
    print("\nMaking a "+str(size)+"-inch pizza with the following toppings: ")
    for topping in toppings:
        print("... "+topping)

make_pizza(5,"pepperoni")
make_pizza(8,"mushroom","green_peppers","extra cheese")