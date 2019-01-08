# Domácí úkol 3 - modul pro práci s GeoJSONem

Deadline je týden před datem, ke kterému chcete zápočet.

## Motivace

Pokud ve svých programech často pracujete s daty ve formátu GeoJSON, je vhodné
si místo jednorázových funkcí napsat třídu, pomocí které budete s GeoJSONem
pracovat. Tato třída vám umožní snadno načítat data ze souboru, zpět je tam
ukládat, procházet je a modifikovat. 

## Zadání

Napište modul geojson, který bude určen pro práci s daty ve formátu GeoJSON.
Pro správnou dědičnost / kompozici jednotlivých tříd vycházejte ze specifikace
[GeoJOSNu][1].

### Třídy
Implementujte tyto třídy:
  * GeoJSON (~ GeoJSON Object)
  * Geometry (~ Geometry Object)
  * Point
  * MultiPoint
  * LineString
  * MultiLineString
  * Polygon
  * MultiPolygon
  * GeometryCollection
  * Feature (~ Feature Object)
  * FeatureCollection (~ FeatureCollection Object)

### Metody a atributy
  * `GeoJSON.loadFromFile(filename)`
    * metoda třídy GeoJSON (`@classmethod`)
    * načte ze souboru jména `filename` GeoJSON a vrátí ho jako objekt třídy GeoJSON
    * jednotlivé části GeoJSONu budou reprezentovány výše uvedenými třídami
  * `gj.saveToFile(filename)`
    * metoda objektu `GeoJSON`
    * uloží objekt `gj` do souboru jména `filename` jako GeoJSON
  * `gj.bbox()` (2 b)
    * metoda objektu `GeoJSON`
    * vrátí čtveřici `(left,bottom,right,top)` reprezentující bounding box všech
      entit uvnitř objektu (např. pro FeatureCollection vrátí bounding box celé
      této kolekce)
  * `obj.__str__()` (2 b)
    * metoda každého objektu
    * měla by vrátit string popisující, co je daný objekt zač a případně co
      obsahuje. Příklady:
	* `FeatureCollection(24 objects, bbox: [14,49,15,51])`
	* `Point(12.253,49.4)`
    * slouží pro programátora, aby při zavolání `print(obj)` věděl, co je `obj` zač
  * `multi.explode()` (1 b)
    * metoda objektů třídy MultiPoint, MultiLineString a MultiPolygon
    * rozbije multigeometrii na jednotlivé geometrické objekty
    * vrátí seznam jednoduchých geometrií (Point / LineString / Polygon), ze
      kterých se složený objekt skládá
  * `obj.__eq__(obj2)` (2 b)
    * metoda každého objektu
    * jako parametr dostane jiný objekt a vrátí `True`, pokud se jedná o stejný
      objekt, jinak `False`
    * stejný objekt je takový, který má stejnou polohu a atributy
    * metoda umožní používat `==` k porovnání dvou objektů
  * `fc.get_by_id(id,default=None)` (1 b)
    * metoda objektu FeatureCollection
    * vrátí ten prvek kolekce, jehož id (viz sekce 3.2 v [dokumentaci][1])
      odpovídá argumentu `id`, v opačném případě vrátí `None`
  
### Ukázkový program

K modulu napište jednoduchý ukázkový program, který využívá všechny metody
vašeho modulu. 

### Další požadavky
Dokumentaci nepište jako samostatný soubor, ale pište ji jako docstringy k
jednotlivým třídám, atributům a metodám.


## Doporučení
Předtím, než začnete programovat, si přečtěte specifikaci GeoJSONu, nebo alespoň
její relevantní části. Následně si nakreslete objektový návrh a rozmyslete se,
co a jak by měly dělat jednotlivé metody. Když exportujete, nepište celý export
v `saveToFile`, ale nechte jednotlivé třídy, aby vám připravily data, která drží
a pak jen spojte tyto výsledky dohromady.

## Bodování
  * 4 b za funkční základ
  * 2 b za kvalitu kódu a správný návrh
  * 1 b za dokumentaci (docstringy)

## Bonusové body

### Používání Gitu pro vývoj (1 b)
Pokud budete pro verzování používat Git, vytvořte si účet na GitHubu nebo jiné
podobné stránce a úkol můžete odevzdat přes něj. Kromě samotného odevzdání je
třeba, aby byl repozitář používán i pro vývoj, tedy by měl obsahovat průběžně
commitovanou práci a jednotlivé commity by měly mít smysluplné commit message,
které popisují, co jste od minulého commitu změnili. Pokud budete potřebovat pomoct,
pište mi.

### Další implementované metody / atributy (?? b)
Viz bodování u metod



[1]: https://tools.ietf.org/html/rfc7946
