#!/usr/bin/python

age = 23
print('happy ' + str(age) + 'rd years old')

print(5+3)
print(int(16/2))
print((16/2).__int__())

a = 'Itry'
b = 3
print(a+b.__str__())


a = ['1', '2', '3', '4']
b = [y for x in a for y in x]
print(b)
