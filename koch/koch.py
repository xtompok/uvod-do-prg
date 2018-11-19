from turtle import pendown,penup,goto,exitonclick
from math import sqrt



def koch(startx,starty,endx,endy,d):
    if d == 0:
        return
    dirx = endx-startx
    diry = endy-starty
    pointA = (startx + dirx/3,starty + diry/3)
    pointB = (startx + 2*dirx/3,starty + 2*diry/3)
    baseC = (startx + dirx/2, starty + diry/2)
    pointCx = baseC[0]-diry/3*sqrt(3)/2
    pointCy = baseC[1]+dirx/3*sqrt(3)/2
    goto(startx,starty)
    pendown()
    goto(pointA[0],pointA[1])
    goto(pointCx,pointCy)
    goto(pointB[0],pointB[1])
    goto(endx,endy)
    penup()
    koch(startx,starty,pointA[0],pointA[1],d-1)
    koch(pointA[0],pointA[1],pointCx,pointCy,d-1)
    koch(pointCx,pointCy,pointB[0],pointB[1],d-1)
    koch(pointB[0],pointB[1],endx,endy,d-1)

penup()
koch(-750,-500,750,-500,5)
exitonclick()




