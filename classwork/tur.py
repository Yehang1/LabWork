import turtle
screen=turtle.Screen()
screen.title('my first drawing')
screen.bgcolor('blue')
pen=turtle.Turtle()
pen.shape('turtle')
pen.width(20)
pen.fillcolor('yellow')
pen.speed(1)
pen.begin_fill()

for i in range(4):
    pen.forward(100)
    pen.right(90)
pen.end_fill()





turtle.done()
