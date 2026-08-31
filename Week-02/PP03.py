# 1. Find the biggest of 3 numbers.
# 2. Write a program

import math

number1 = int(input("Enter the value of number1: "))
operator = input("Enter the operator: ")
number2 = int(input("Enter the value of number2: "))

if number1 or number2 == 0 and operator == "*" or operator == "/":
    print("Invalid")
    exit()

if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
else:
    print("Operator not supported")
