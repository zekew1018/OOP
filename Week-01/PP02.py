
number1 = int(input("Enter the value of number1: ")) #Signs like "=" are assigning symbols, "==" and "!=" is a conditional symbol
number2 = int(input("Enter the value of number2: "))
number3 = int(input("Enter the value of number3: "))
print("Thank You.")
# 1. Find the biggest of the three numbers
# 2. Find the smallest of the three numbers

#greatest number search
if number1 > number2 and number1 > number3:
    print("number1 is the greatest value.")
elif number2 > number1 and number2 > number3:
    print("number2 is the greatest value.")
elif number3 > number1 and number3 > number2:
    print("number3 is the greatest value.")
elif number1 == number2 and number1 == number3:
    print("Values are equal.")
elif number1 == number2 and number3 > number1:
    print("number3 is the greatest value.")
elif number1 == number3 and number2 > number1:
    print("number2 is the greatest value.")
elif number3 == number2 and number1 > number2:
    print("number1 is the greatest value.")
#smallest number search
print("")
if number1 < number2 and number1 < number3:
    print("number1 is the smallest value.")
elif number2 < number1 and number2 < number3:
    print("number2 is the smallest value.")
elif number3 < number1 and number3 < number2:
    print("number3 is the smallest value.")
elif number1 == number2 and number3 < number1:
    print("number3 is the smallest value.")
elif number1 == number3 and number2 < number1:
    print("number2 is the smallest value.")
elif number3 == number2 and number1 < number2:
    print("number1 is the smallest value.")

a = 4
b = 3
c = 2
d = 1
e = 1

# if number1 > number2:
#    print("They are not equal, number1 is greater than number2")
#elif number1 == number2:
#    print("number1 is equal to number2")
#elif number1 < number2:
#    print("They are not equal, number1 is less than number2")
#else:
#    print("They are not equal, number2 is greater than number1")

#if a > b and c > d or e == d:
#    print("Statement")