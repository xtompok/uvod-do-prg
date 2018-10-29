import json

def zastavky_v_pasmu(zastavky,pasmo):
	jmena = []
	for z in zastavky:
		props = z["properties"]
		if props["ZAST_PASMO"] is None:
			continue
		if pasmo in props["ZAST_PASMO"]:
			jmena.append(props["ZAST_NAZEV"])
	return jmena

with open("DOP_PID_ZASTAVKY_B.json",encoding="utf-8") as f:
    zastavky = json.load(f)

features = zastavky["features"]
zastavky_P = zastavky_v_pasmu(features,"P")
print(zastavky_P)
