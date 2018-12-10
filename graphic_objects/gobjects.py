from graphic_objects import Point,Polyline,Polygon,Rectangle, LineSegment
import turtle

pt = Point(0,0)
l = Polyline([Point(10,10),Point(70,100)])
pg = Polygon([Point(20,34),Point(-50,65),Point(100,100)])
rect = Rectangle(Point(-10,-10),Point(20,30))
seg = LineSegment(Point(-20,-20),Point(12,45))
turtle.penup()

pt.draw()
l.draw()
pg.draw()
rect.draw()
seg.draw()

turtle.exitonclick()