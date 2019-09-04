#!/usr/bin/python


def make_car(manufacturer, model, **car_info):
    car = {}
    car['manufacturer'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car


mycar = make_car("VW", "Audi", color="Black", tow_package=True)

print(mycar)
