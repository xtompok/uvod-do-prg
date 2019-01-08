# Úvod do programování
Zdrojové kódy a poznámky ke cvičení z Úvodu do programování.

[Stránky](http://web.natur.cuni.cz/~bayertom/index.php/9-teaching/10-uvod-do-programovani) přednášky.

Věci probírané na jednotlivých cvičeních najdete na [samostatné stránce](prubeh.md).
Cvičení probíhá rámcově podle kurzu [Nauč se Python!](https://naucse.python.cz/course/pyladies/).

Cvičení probíhá v jazyku Python 3. Možná jste se setkali, například na Programování pro GIS, s Pythonem 2, pak pozor, jazyky jsou podobné, ale ne stejné, například `print` v Pythonu 3 se vždy volá se závorkami.

## Programové vybavení
Na cvičení budeme programovat v Pythonu 3 v prostředí [PyCharm](https://www.jetbrains.com/pycharm/), stáhněte si zdarma dostupnou Community Edition. Můžete samozřejmě použít i jiná prostředí, pokud jsou vám bližší.

Pro základní pochopení struktury programů si můžete vyzkoušet například [Google Blockly](https://developers.google.com/blockly/).

## Základy syntaxe 
 - příkazy oddělené koncem řádku
 - proměnné
   - vznikají prvním přiřazením pomocí `=`
 - blok kódu
   - seznam příkazů vykonávaných za nějaké situace (podmínka, cyklus)
   - oddělený odsazením
     - 4 mezery nebo tabulátor
     - musí být konzistentní v celém zdrojovém kódu
 - porovnání vs. přiřazení
   - `=` je přiřazení, výsledkem je hodnota přiřazeného výrazu
   - `==` je porovnání, výsledek je pravda, pokud se levá strana rovná pravé, nepravda jinak
   - porovnáváme pouze proměnné stejných typů, porovnání čísla a řetězce je vždy nepravda
 - podmínka
```
if <vyraz>:
  <blok>
```
   - pokud je `<vyraz>` splněn, pak se vykoná `<blok>`

## Typy
   - `str` - řetězec znaků
     - `'text'`
     - `"text"`
     - `"""text"""` - může obsahovat konce řádků
   - `int` - celé číslo
   - `float` - desetinné číslo, odpovídá `double` z jiných jazyků
   - typ proměnné zjistíte zavoláním `type(promenna)`
 - převody mezi typy:
   - `str(promenna)` - cokoli -> string
   - `int(promenna)` - řetězec -> int
   - `float(promenna)` - řetězec -> float

## Moduly a funkce v nich
 - v modulech jsou obsažené další rozšiřující funkce
 - můžeme buď importovat modul a pak funkce z něj používat jako `modul.funkce`
```
import math
odmocnina_z_peti = math.sqrt(5)
```
 - nebo můžeme importovat z modulu konkrétní funkci a pak ji používat přímo
```
from math import sqrt
odmocnina_z_peti = sqrt(5)
```

## Vstup a výstup
 - výpis na obrazovku
   - `print(obsah)`
     - obsah může být libovolného typu
    
 - čtení z konzole
   - `input(prompt)`
     - vypíše parametr `prompt`, vrací načtený řádek (bez konce řádku) jako `str`

### Formátování řetězců
 - `"{} je rovno priblizne {:.2f}".format("π",math.pi)`
 - v řetězci na místo, kam chceme vložit proměnnou, napíšeme `{}`
 - za řetězec přidáme `.format()` a do závorek napíšeme proměnné v tom pořadí, v jakém je chceme dosadit do řetězce
 - pro formátování desetinných čísel (a jiné formátování) můžeme použít [modifikátory](https://docs.python.org/3/library/string.html#formatstrings) uvnitř složených závorek
   - nejčastěji `{:.2f}`
     - za desetinnou tečkou budou 2 platné číslice
     - číslo se vypíše jako float
 - lze formátovat libovolný řetězec, ne jen v printu


## Aritmetika
 - používáme se standardní matematické operátory
 - `**` je umocnění
 - mnoho užitečných funkcí najdete v modulu [math](https://docs.python.org/3.7/library/math.html)

## JSON a GeoJSON
 - formát pro ukládání dat
 - původně vznikl v rámci JavaScriptu
 - [specifikace JSONu](https://www.json.org/)
 - datové typy podobné typům v Pythonu
   - true, false, null
   - čísla
   - řetězce
   - array (seznam)
   - object (slovník)
 - GeoJSON je způsob ukládání geodat pomocí JSONu
 - [specifikace GeoJSONu](https://tools.ietf.org/html/rfc7946)
 - data v GeoJSONu lze snadno vložit na web pomocí knihovny Leaflet

## Rekurze
 - způsob, jak převést řešení problému na řešení menších podproblémů
 - funkce řešící nějaký problém vyřeší jeho část a zavolá sama sebe na nějaký(é) jednodušší podproblém(y)
 - je potřeba definovat koncovou podmínku, kdy už vyřešíme celý zbytek problému, aby se funkce nevolala donekonečna

## Předávání vstupu programům
 - program obvykle potřebuje nějaká vstupní data, se kterými pak dále počítá
 - existují různé způsoby, jak tato data programu předat:
     - interaktivně (pomocí `input`)
         - vhodné, pokud s programem pracuje přímo uživatel
	 - možnost opakovat zadání při chybném vstupu
	 - nevhodné pro automatické spouštění
     - čtení z pevně zadaného souboru
         - jednoduché na implementaci
	 - vhodné pro automatické spouštění
	 - pokud máme více vstupních souborů, musíme je mezi jednotlivými spuštěními přejmenovávat, což je náchylné na chyby
     - předání argumentů na příkazové řádce
         - vhodné pro automatické spouštění
	 - umožňuje snadno parametrizovat běh programu i při automatickém spouštění
	 - náročnější na implementaci

## Práce s argumenty příkazové řádky
 - je potřeba importovat modul `sys`
 - `sys.argv` obsahuje seznam všech argumentů
   - `sys.argv[0]` je jméno programu, pomocí kterého byl spuštěn
   - od `sys.argv[1]` začínají jednotlivé argumenty, v tom pořadí v jakém byly zadány
 - soubory se zadávají obvykle svým jménem
 - parametry ovlivňující běh programu obvykle jako `-<pismeno> [hodnota]`
   - `pismeno` je písmeno určující, který parametr chceme nastavit
   - `hodnota` (volitelná) je hodnota, na kterou chceme parametr nastavit
 - pro příjemnější práci s argumenty se hodí modul `click`

## Užitečné moduly
 - práce se shapefily: Fiona (https://fiona.readthedocs.io/en/latest/)
 - zpracování argumentů příkazové řádky: Click (https://click.palletsprojects.com/en/7.x/)
 - stahování dat z webu: urllib (obsažena ve výchozí instalaci Pythonu)
 - práce s rastrovámi daty: Pillow (https://pillow.readthedocs.io/en/stable/)
