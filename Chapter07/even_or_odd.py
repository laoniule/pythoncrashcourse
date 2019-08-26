number = input("Enter a number and I'll tel you it's even or odd:  ")
number = int(number)

if number%2 == 0:
    print(str(number)+" is an even")
else:
    print(str(number)+" is an odd")