import random
import turtle


def generate_data(n=100):
    data = []
    for _ in range(n):
        data.append((random.random(),random.random()))
    return data

def show_data(data):
    turtle.speed(0)
    turtle.hideturtle()
    turtle.penup()
    for pt in data:
        turtle.setposition(pt[0]*300,pt[1]*300)
        turtle.dot()

data = generate_data()
show_data(data)
# Sem vložte kod pro clusterovani
turtle.exitonclick()