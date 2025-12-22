import turtle

def octagon(length):
    for i in range(8):
        turtle.forward(length)
        turtle.left(45)

def rectangle(width, height):
    for i in range(2):
        turtle.forward(width)
        turtle.right(90)
        turtle.forward(height)
        turtle.right(90)

def stop(length):
    octagon(length)
    turtle.forward(length*(3/8))
    rectangle(length/5, length*2)

def main():
    stop(100)
    turtle.color("red")
    turtle.penup()
    turtle.forward(200)
    turtle.pendown()
    stop(50)

main()
turtle.Screen().exitonclick()