#!/sur/bin/python

prompt = "If you could visit oneplace in the world,where would you go?"

favorite_places = {}

polling_avtive = True
while polling_avtive:
    name = input("\nWhat is your name?")
    reponse = input(prompt)

    favorite_places[name] = reponse

    repeat = input("if another person response?(yes or no)")
    if repeat.lower() == "no":
        polling_avtive = False
    
print(favorite_places)