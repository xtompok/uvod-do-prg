from math import floor
deg = float(input("Zadej stupne: "))

# floor dela dolni celou cast
intdeg = floor(deg)
amin = (deg-intdeg)*60
intmin = floor(amin)
sec = (amin-intmin)*60

if amin == 0 and sec == 0:
    print(intdeg,"°")
elif sec == 0:
    print(intdeg,"°",intmin,"'")
else:
    print("{}° {}' {:.2f}\"".format(intdeg,intmin,sec))