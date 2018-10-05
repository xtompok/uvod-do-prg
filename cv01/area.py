import math

atype = input("Zadej typ útvaru(čtverec, kruh): ")
if atype == "čtverec":
    side = float(input("Zadej délku strany: "))
    area = side**2
    print("Plocha je {:.2f}".format(area))
elif atype == "kruh":
    r = float(input("Zadej poloměr: "))
    area = math.pi * r * r
    print("Plocha je {:.2f}".format(area))
else:
    print("Zadal jsi špatný útvar")
