import turtle



def make_square(side):
    turtle.pendown()
    for _ in range(4):

        turtle.forward(side)
        turtle.left(90)
    turtle.penup()
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(10)
    turtle.left(180)


def main():
    side = 20
    for _ in range (5):
        make_square(side)
        side = side + 20
        
if __name__ == "__main__":
        main()