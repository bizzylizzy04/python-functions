import math

# Get input from the user
num = float(input("Please enter a number: "))

# a. Absolute value
print("absolute value:", abs(num))

# b. Number rounded to 0 decimal places
print("rounded to 0:", round(num, 0))

# c. Square root of the rounded number’s absolute value
sqrt_val = math.sqrt(abs(num))
print("square root:", math.sqrt(abs(round(num, 0))))