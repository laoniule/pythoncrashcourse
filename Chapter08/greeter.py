#!/usr/bin/python


def get_formatted_name(first_name, last_name):
    full_name = first_name + " " + last_name
    return full_name.title()


while True:
    print("\nPlease tell me your name.")
    print("(enter 'q' at any time to quit)")

    fname = input("First_name: ")
    if fname == 'q':
        break

    lname = input("Last name: ")
    if lname == "q":
        break

    formatted_name = get_formatted_name(fname, lname)
    print("\nHello, " + formatted_name + "!")
