import math as Math;
#
# Level 1: Basic Python (1–10)
#
# Hello World: Write a Python program to print Hello, World!.
#
print('Hello World')
# Personal Details: Print your name, age, and city on separate lines.
#
print('My Name is Sudip')
print('My age is 30')
print("I live in kathmandu, Nepal")
# Add Two Numbers: Take two numbers as input and print their sum.
#
x = int(input("Enter the first Number: "))
y = int(input("Enter the second Number: "))
sum = x+ y
print(f"The sum of {x} and {y} is {sum}")
# Arithmetic Operations: Take two numbers and print their sum, difference, product, and division.
#
print(f"The  Subtraction of {x} and {y} is {x - y}")

print(f"The multiplication of {x} and {y} is {x * y}")

print(f"The division of {x} and {y} is {x / y}")

# Square of a Number: Take a number and print its square and cube.
#
print(f"The Square of {x} is {x ** 2}")

print(f"The Cube of {x} is {x ** 3}")

# Area of a Rectangle: Take length and width and calculate the area.
#
print (f"The area of rectangle is {x*y}")
# Area of a Circle: Take the radius and calculate the area using π = 3.14.
#
print(f"The Area Of Circle is {float(Math.ceil(x*3.14))}")
# Swap Two Variables: Swap the values of two variables.
#
a , b = 10 , 40
print(f"The Number before swap is {a} and {b}")
b, a = a, b
print(f"The swap of {a} and {b} is completed")
# Celsius to Fahrenheit: Convert Celsius temperature to Fahrenheit.
#

# Simple Interest: Calculate simple interest using principal, rate, and time.