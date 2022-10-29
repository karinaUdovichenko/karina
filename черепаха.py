import turtle

s = 300
n = 2


def kriv(size, n):
    if n == 0:
        turtle.forward(size)
    else:
        kriv(size / 3, n - 1)
        turtle.left(60)
        kriv(size / 3, n - 1)
        turtle.right(120)
        kriv(size / 3, n - 1)
        turtle.left(60)
        kriv(size / 3, n - 1)


def draw(size, n):
    for i in range(3):
        kriv(size, n)
        turtle.right(120)


draw(s, n)
