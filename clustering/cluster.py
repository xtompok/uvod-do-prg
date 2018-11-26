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

def split(data):
    ''' Rozdeli data na pul podle souradnice x
    Vraci x souradnici, podle ktere data rozdelit'''
    data = sorted(data, key=lambda x: x[0])
    half = len(data)//2
    return (data[half][0]+data[half+1][0])/2


data = generate_data()
show_data(data)
# Sem vložte kod pro clusterovani
x = split(data)
turtle.setposition(300*x,0)
turtle.pendown()
turtle.setposition(300*x,300)
turtle.exitonclick()