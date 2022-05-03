import turtle
def drawFlower(numOfSquares):
    turt = turtle.Turtle()
    turt.speed(15)
    turt.color("pink", "yellow")
    turt.begin_fill()
    for i in range(numOfSquares):
        for k in range(4):
            turt.forward(65)
            turt.left(90)
        turt.forward(65)
        turt.right(360 / numOfSquares)
    turt.end_fill()
    turt.color("yellow", "brown")
    turt.begin_fill()
    center = 360 / numOfSquares
    for i in range(numOfSquares):
        turt.forward(65)
        turt.right(center)
    turt.end_fill()
    turt.getscreen().mainloop()
def main():
    numOfSquares = int(input("How many Petals would you like? \n"))
    drawFlower(numOfSquares)
main()