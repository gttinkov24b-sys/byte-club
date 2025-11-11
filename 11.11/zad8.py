import turtle
t = turtle.Turtle()
t.width(3)
t.speed(5)

t.fillcolor("blue")
t.begin_fill()
for i in range(5):
    t.forward(225)
    t.right(144)
t.end_fill()
t.right(36)
turtle.done()
