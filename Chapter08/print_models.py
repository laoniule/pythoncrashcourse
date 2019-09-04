#!/usr/bin/python

# unprinted_designs = ['iphone case','robot pendant','dodecahedron']
# completed_models=[]

# while unprinted_designs:
#     current_design = unprinted_designs.pop()

#     print("Printing model: " +current_design)
#     completed_models.append(current_design)


# print("\nThe follow models have been printed:")
# for printed_model in completed_models:
#     print(printed_model)


def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()

        print("Printing model: " + current_design)
        completed_models.append(current_design)


def show_completed_models(completed_models):
    print("\nThe follow models have been printed:")
    for printed_model in completed_models:
        print(printed_model)


# unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# print(unprinted_designs)
# print(completed_models)
