import turtle
from abc import ABC,abstractmethod

def calcBbox(points):
    left = min(map(lambda pt: pt.x,points))
    right = max(map(lambda pt: pt.x,points))
    bottom = min(map(lambda pt: pt.y,points))
    top = max(map(lambda pt: pt.y,points))
    ll = Point(left,bottom)
    ur = Point(right,top)
    return Rectangle(ll,ur)

class GraphicObject(ABC):
    @abstractmethod
    def draw(self):
        pass

class Point(GraphicObject):
    def __init__(self,ax=0,ay=0,color = "black"):
        self.x = ax
        self.y = ay
        self.color = color

    def draw(self):
        turtle.pencolor(self.color)
        turtle.goto(self.x,self.y)
        turtle.dot(3)

    def __str__(self):
        return "Point ({},{})".format(self.x,self.y)

class Polyline(GraphicObject):
    def __init__(self,points,color="black"):
        self.pts = points
        self.color = color
        self.bbox = calcBbox(points)

    def draw(self):
        turtle.goto(self.pts[0].x,self.pts[0].y)
        turtle.pencolor(self.color)
        turtle.pendown()
        for p in self.pts:
            turtle.goto(p.x,p.y)
        turtle.penup()

    def __str__(self):
        return "Polyline ({} points)".format(len(self.pts))


class Polygon(GraphicObject):
    def __init__(self,points,color="black"):
        self.pts = points
        self.color = color
        self.bbox = calcBbox(points)

    def draw(self):
        turtle.goto(self.pts[0].x,self.pts[0].y)
        turtle.pencolor(self.color)
        turtle.pendown()
        for p in self.pts:
            turtle.goto(p.x,p.y)
        turtle.goto(self.pts[0].x,self.pts[0].y)
        turtle.penup()

    def __str__(self):
        return "Polygon ({} points)".format(len(self.pts))

class Rectangle(Polygon):
    def __init__(self,ll,ur,color="black"):
        lr = Point(ur.x,ll.y)
        ul = Point(ll.x,ur.y)
        pts = [ll,lr,ur,ul]
        self.pts = pts
        self.color = color
        self.bbox = self


    def __str__(self):
        return "Rectangle ({},{})".format(self.ll,self.ur)

class LineSegment(Polyline):
    def __init__(self,p1,p2,color="black"):
        pts = [p1,p2]
        super().__init__(pts,color)

    def __str__(self):
        return "Line segment ({} - {})".format(self.pts[0],self.pts[1])

