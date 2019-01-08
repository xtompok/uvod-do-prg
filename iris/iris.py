from urllib.request import urlopen
import json
import turtle

addr = "http://iris.bmhd.cz/api/data.json"

turtle.setworldcoordinates(16.5,49.12,16.7,49.25)
turtle.speed(0)
turtle.penup()
turtle.hideturtle()

strdata = urlopen(addr)
dictdata = json.load(strdata)

for (aid,props) in dictdata["Data"].items():
    print("{}: {} N, {} E".format(aid,props["Lat"],props["Lng"]))
    # Chceme jen tramvaje => aid < 2000
    if int(aid) >= 2000:
        continue
    turtle.goto(props["Lng"],props["Lat"])
    turtle.dot()

turtle.exitonclick()

#for aid in dictdata["Data"]:
#    props = dictdata["Data"][aid]
#    print("{}: {} N, {} E".format(aid,props["Lat"],props["Lng"]))
