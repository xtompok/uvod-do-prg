hlasya = 0
hlasyb = 0
hlasyc = 0
hlasyd = 0

strana = "xxx"

while strana != "":
    strana = input("Zadej stranu: ")

    # Pokud jsme jen odenterovali, skončíme
    if strana == "":
        break
    # Pokud jsme nezadali žádnou ze stran, ptáme se znovu
    if strana != "a" and strana != "b" and strana != "c" and strana != "d":
        continue

    hlasystr = input("Zadej počet hlasů: ")
    hlasy = int(hlasystr)
    # lze i hlasy = int(input("Zadej počet hlasů: "))

    if strana == "a":
        hlasya += hlasy # == hlasya = hlasya + hlasy
    elif strana == "b":
        hlasyb += hlasy
    elif strana == "c":
        hlasyc += hlasy
    elif strana == "d":
        hlasyd += hlasy

print("Strana a získala {} hlasů".format(hlasya))
print("Strana b získala {} hlasů".format(hlasyb))
print("Strana c získala {} hlasů".format(hlasyc))
print("Strana d získala {} hlasů".format(hlasyd))

