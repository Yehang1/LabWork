import turtle
pen=turtle.Turtle()
pen.shape('turtle')
pen.color('red')
pen.width(10)
pen.fillcolor('blue')
pen.speed(1)
pen.begin_fill()
for i in range(5):
    pen.forward(100)
    pen.right(144)
pen.end_fill()
turtle.done()

