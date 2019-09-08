#! /usr/bin/python

print("Enter 2 number, do divide operation.")
print("Enter Q to exit.")

while True:
    first_number = input("\nfirst number: ")
    if (first_number == 'q' or first_number == 'Q'):
        break
    second_number = input("\nsecond number: ")
    if (second_number == 'q' or second_number == 'Q'):
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cant divide by zero!")
    else:
        print(answer)