import json
import csv

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
with open("zastavky-out.txt",mode="w") as f:
    writer = csv.writer(f)
    for z in zastavky_P:
        #f.write(z)
        #f.write('\n')
        #print(z, file=f)
        writer.writerow([z])

with open("zastavky-out.json",mode="w") as f:
    json.dump(zastavky,f)


def uloz_nasobnosti(nas):
    with open("nasobnosti-out.txt",mode="w") as f:
        writer = csv.writer(f)
        #for k,v in nas.items():
        #    writer.writerow([k,v])
        writer.writerows(nas.items())

nas = {"Anděl":10, "Zlíchov":4, "Lihovar":2}
nas = {}
for z in zastavky_P:
    if z not in nas:
        nas[z] = 1
    else:
        nas[z] += 1
        
uloz_nasobnosti(nas)

exit()
