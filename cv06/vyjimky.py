

def vnitrni_funkce():
    print("Vstupuji")
    c = 1/0.0000
    print("Vystupuji")
    return c

def vnejsi_funkce():
    print("Vstupuji")
    d = vnitrni_funkce()
    print("Vystupuji")
    return d

try:
    #res = vnejsi_funkce()
    res = int(input("Zadej cislo: "))
except ValueError:
    print("Chyba!")
    exit(1)

try:
    vystup = 42/res
except ZeroDivisionError:
    print("Deleni nulou!")
    vystup = float("inf")

print("Za vodou")
print(vystup)