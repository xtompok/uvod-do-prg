import turtle
from abc import ABC,abstractmethod

class GraphicObject(ABC):
    @abstractmethod
    def draw(self):
        pass

class Point(GraphicObject):
    def __init__(self,ax=0,ay=0):
        self.x = ax
        self.y = ay

    def draw(self):
        turtle.goto(self.x,self.y)
        turtle.dot(3)

    def __str__(self):
        return "Point ({},{})".format(self.x,self.y)

class Polyline(GraphicObject):
    def __init__(self,points):
        self.pts = points

    def draw(self):
        turtle.goto(self.pts[0].x,self.pts[0].y)
        turtle.pendown()
        for p in self.pts:
            turtle.goto(p.x,p.y)
        turtle.penup()

    def __str__(self):
        return "Polyline ({} points)".format(len(self.pts))

class Polygon(GraphicObject):
    def __init__(self,points):
        self.pts = points

    def draw(self):
        turtle.goto(self.pts[0].x,self.pts[0].y)
        turtle.pendown()
        for p in self.pts:
            turtle.goto(p.x,p.y)
        turtle.goto(self.pts[0].x,self.pts[0].y)
        turtle.penup()

    def __str__(self):
        return "Polygon ({} points)".format(len(self.pts))

class Rectangle(Polygon):
    def __init__(self,ll,ur):
        lr = Point(ur.x,ll.y)
        ul = Point(ll.x,ur.y)
        self.pts = [ll,lr,ur,ul]

    def __str__(self):
        return "Rectangle ({},{})".format(self.ll,self.ur)

class LineSegment(Polyline):
    def __init__(self,p1,p2):
        self.pts = [p1,p2]

    def __str__(self):
        return "Line segment ({} - {})".format(self.pts[0],self.pts[1])