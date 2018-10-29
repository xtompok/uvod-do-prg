import json

# Takto můžete vytvořit slovník
z= {"jmeno":"Albertov",
    "pasmo":"P",
    "seznam_linek":[7, 18, 14, 24, 93],
    "prist": True,
    "ID":"1643Z23"}
print(z)

# Test na existenci klíče "ID" ve slovníku z
if "ID" in z:
    print("Id je {}".format(z["ID"]))
else:
    print("Id nepritomno")

# Iterace přes klíče
for k in z:
    print("{} = {}".format(k,z[k]))

# Iterace přes dvojice (klíč, hodnota)
for k,v in z.items():
    print("{} = {}".format(k,v))

k,v = ("Jmeno","Albertov")
print(k,v)

# Slovník jako nástroj pro překlad
znamky = {1: "výborně", 2: "ujde", 3:"neprospěl"}
print("Hodnoceno {}".format(znamky[2]))

# Čtení souboru
f = open("a.txt")
print(f.read())
f.close() # nezapomenout soubor zavřít

# Načtení GeoJSONu
with open("DOP_PID_ZASTAVKY_B.json",encoding="utf-8") as f:
    zastavky = json.load(f)

# Práce s GeoJSONem
# Tady muzu neco pocitat a soubor uz je zavreny
print(type(zastavky))
for k in zastavky:
    print(k)

features = zastavky["features"]
print(type(zastavky["features"]))

