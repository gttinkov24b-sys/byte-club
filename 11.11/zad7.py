import turtle
t = turtle.Turtle()
t.width(3)
t.speed(5)

t.fillcolor("indigo")
t.begin_fill()
for i in range(4):
    t.forward(300)
    t.right(90)
t.end_fill()

turtle.done()
