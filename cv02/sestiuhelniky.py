from turtle import forward, left, right,exitonclick

xsize = 5
ysize = 5


for i in range(xsize):
    for i in range(ysize):
        for i in range(6):
            forward(50)
            left(60)
        forward(50)
        left(60)
        forward(50)
        right(60)
    left(180)
    for i in range(ysize):
        left(60)
        forward(50)
        right(60)
        forward(50)
    left(60)
    forward(50)
    left(60)
    forward(50)
    left(60)


exitonclick()