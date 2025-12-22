# a) 1, 2, 3, 4, 5
for i in range(1, 6):
    print(i)
print()  # Print a blank line

# b) 2, 5, 8, 11
for i in range(2, 12, 3):
    print(i)
print()  # Print a blank line

# c) -10, -8, -6, -4, -2, 0
for i in range(-10, 1, 2):
    print(i, end=" ")
print()  # Print a blank line

# d) ****, ****, ****, ****
for i in range(4):
    print("****")
print()  # Print a blank line

################
# Write a for loop that prints the letters in “CSCI 150” on separate lines.
for letter in "CSCI 150":
    print(letter)

print()  # Print a blank line

################
# Using the range function, print the numbers from 1 to 10 (inclusive). Each number should be on a separate line.
for i in range(1, 11):
    print(i)
print() # Print a blank line

################
# Using the range function, print the multiples of 5 from 10 through 25 (inclusive). The numbers should each be separated by a space. (Hint: use the end parameter to the print function like we did in for_range.py). Don’t forget to print a newline after this loop by calling print() with no parameters.
for i in range(10, 26, 5):
    print(i, end=" ")

print()  # prints a newline after the loop

# Using the range function, print the multiples of 3 from -3 to 21 (inclusive). Each number should be separated by a comma and a space. There should not be a comma after the final number (21).
for i in range(-3, 22, 3):
    print(i, end=", " if i < 21 else "\n")

print()  # Print a blank line

saying = "howdy"
for u in saying.upper():
    print(saying, end=" ")

print()