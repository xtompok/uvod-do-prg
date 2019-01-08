from urllib.request import urlopen
import json

# Stažení souboru s pevnou adresou a jeho zpracování
address = "http://opendata.iprpraha.cz/CUR/FSB/BEZ_OkrskyMPP_p/WGS_84/BEZ_OkrskyMPP_p.json"
data = urlopen(address)
okrsky = json.load(data)
for o in okrsky['features']:
    print(o['properties']['MC_PRAHA'])

# Stahování dat ze SRTM, jména souborů jsou odvoditelná a
# generována dynamicky dle požadovaného rozsahu dat
base="https://dds.cr.usgs.gov/srtm/version2_1/SRTM3/Eurasia/"
minlat = 47
maxlat = 51
minlon = 14
maxlon = 18
for lat in range(minlat,maxlat):
    for lon in range(minlon,maxlon):
        filename = "N{:02}E{:03}.hgt.zip".format(lat,lon)
        data = urlopen(base+filename)
        with open(filename,"wb") as f:
            f.write(data.read())


