#!/usr/bin/python


def city_country(city, country):
    cityCountry = {city,  country}
    return cityCountry


while True:
    print('\nEnter Q to exit')

    var_city = input("\nPlease input your city: ")
    if var_city.lower() == "q":
        break
    var_country = input("\nPlease input you country: ")
    if var_country.lower() == "q":
        break
    print(city_country(var_city, var_country))
