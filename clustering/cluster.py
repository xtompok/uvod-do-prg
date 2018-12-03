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

def get_x_half(data):
    ''' Najde x souradnici, ktera deli body napul podle x
    Vraci x souradnici, podle ktere data rozdelit'''
    data = sorted(data, key=lambda x: x[0])
    half = len(data)//2
    return (data[half][0]+data[half-1][0])/2

def get_y_half(data):
    ''' Najde y souradnici, ktera deli body napul podle y
    Vraci y souradnici, podle ktere data rozdelit'''
    data = sorted(data, key=lambda x: x[1])
    half = len(data)//2
    return (data[half][1]+data[half-1][1])/2

def split_x(data,x):
    '''Rozdeli data na 2 seznamy podle x souradnice
    Vraci (seznam_vlevo_od_x, seznam_vpravo_od_x)'''
    s1 = []
    s2 = []
    for pt in data:
        if pt[0] < x:
            s1.append(pt)
        else:
            s2.append(pt)
    return s1,s2

def split_y(data,y):
    '''Rozdeli data na 2 seznamy podle y souradnice
    Vraci (seznam_dolu_od_y, seznam_nahoru_od_y'''
    s1 = []
    s2 = []
    for pt in data:
        if pt[1] < y:
            s1.append(pt)
        else:
            s2.append(pt)
    return s1,s2

def kd_x(data):
    if len(data) < 2:
        return
    x = get_x_half(data)
    draw(data,x=x)
    (left,right) = split_x(data,x)
    kd_y(left)
    kd_y(right)

def kd_y(data):
    if len(data) < 2:
        return
    y = get_y_half(data)
    draw(data,y=y)
    (down,up) = split_y(data,y)
    kd_x(down)
    kd_y(up)


def calc_bbox(data):
    minx = float("inf")
    miny = float("inf")
    maxx = float("-inf")
    maxy = float("-inf")
    for p in data:
        if p[0] < minx:
            minx = p[0]
        if p[0] > maxx:
            maxx = p[0]
        if p[1] < miny:
            miny = p[1]
        if p[1] > maxy:
            maxy = p[1]
    return (minx,miny,maxx,maxy)


def draw(data,x=None,y=None):
    bbox = calc_bbox(data)
    if x:
        turtle.setposition(x*300,bbox[1]*300)
        turtle.pendown()
        turtle.setposition(x*300,bbox[3]*300)
    if y:
        turtle.setposition(bbox[0]*300,y*300)
        turtle.pendown()
        turtle.setposition(bbox[2]*300,y*300)
    turtle.penup()

turtle.speed(0)
data = generate_data(100)
show_data(data)
turtle.speed(2)
# Sem vložte kod pro clusterovani
kd_x(data)
#x = get_x_half(data)
#turtle.setposition(300*x,0)
#turtle.pendown()
#turtle.setposition(300*x,300)
#
#turtle.penup()
#y = get_y_half(data)
#turtle.setposition(0,300*y)
#turtle.pendown()
#turtle.setposition(300,300*y)

turtle.exitonclick()
