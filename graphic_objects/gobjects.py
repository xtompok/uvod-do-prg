from graphic_objects import Point,Polyline,Polygon,Rectangle, LineSegment
import turtle

pt = Point(0,0,"purple")
l = Polyline([Point(10,10),Point(70,100)],"red")
pg = Polygon([Point(20,34),Point(-50,65),Point(100,100)],"green")
rect = Rectangle(Point(-10,-10),Point(20,30),"yellow")
seg = LineSegment(Point(-20,-20),Point(12,45),"pink")
turtle.penup()

pt.draw()
l.draw()
l.bbox.draw()
pg.draw()
pg.bbox.draw()
rect.draw()
seg.draw()
seg.bbox.draw()

turtle.exitonclick()