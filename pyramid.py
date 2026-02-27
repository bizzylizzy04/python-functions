def pyramid(symbol, height):
    for i in range(1, height + 1):
        print(symbol * i)

pyramid("*", 2)
pyramid("+", 5)
pyramid("x", 10)