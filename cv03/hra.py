import random

def osloveni(jmeno):
    if jmeno == 'Marek':
        return jmeno[:-2] + 'ku'
    elif jmeno in ("Jiri", "Samo"):
        return jmeno
    elif jmeno in ("Juraj", "Daniel"):
        return jmeno + 'i'
    elif jmeno in ("Michal", "David", "Filip", "Jakub"):
        return jmeno + 'e'
    else:
        return jmeno[0:len(jmeno)-1] + 'o'

reseni = random.randint(1, 100)
max_pokusu = 7
vyhral = False

jmeno = input("Zadejte sve jmeno:")

print("Vitej ve hre, " + osloveni(jmeno))

zbyva_pokusu = max_pokusu
while zbyva_pokusu > 0:
    hodnota = int (input('cislo? >'))
    if hodnota == reseni:
        print('Uhodl(a)s.')
        vyhral = True
        break
    elif (hodnota < 1) or (hodnota > 100):
        print('To asi ne...')
        continue
    elif reseni > hodnota:
        print('Hadej vetsi.')
    elif reseni < hodnota:
        print('Hadej mensi.')
    zbyva_pokusu = zbyva_pokusu - 1

    if zbyva_pokusu < 4:
        o = osloveni(jmeno) + "! "
        opakovani = 4 - zbyva_pokusu
        print(o * opakovani)

print("KONEC HRY.")
if vyhral:
    print(osloveni(jmeno) + ", vyhral(a) jsi.")
else:
    print(osloveni(jmeno) + ", priste to uz vyjde :-)")

