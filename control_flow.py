#def add(x, y):
#    print("I will add the numbers %d and %d" % (x, y))
#    return x + y;
#sum = add(5, 7) # execution starts here, 5 & 7 (actual parameters) are passed to x & y (formal parameters)
#print("=", sum)

def add(x, y):
    return x + y;

def multiply(x, y):
    return x * y;

#print(add(5, 7))
#print(multiply(5, 7))

def main():
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    total = add(num1, num2)
    product = multiply(num1, num2)

    print("Sum:", total)
    print("Product:", product)

main()