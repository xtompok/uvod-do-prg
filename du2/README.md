# Domácí úkol 2 - dělení adresních bodů

Deadline bude 16. 12. 2018 v 8.03.

## Motivace

V některých situacích nechceme zpracovávat data pro každou jednu jednotku, ale
chceme z jednotek vytvořit skupiny a zpracovávat data dohromady pro celou
skupinu, například pro vyloučení extrémních případů. Jednotky chceme seskupovat
do skupin tak, aby vzniklé skupiny byly kompaktní a nebyly složeny z jednotek
roztroušených po celé mapě a měly nějakou maximální velikost.

## Zadání

Napište neinteraktivní program, který bude metodou quadtree dělit data do skupin
tak, aby žádná skupina neměla více než 50 jednotek. Program dostane jako
argumenty vstupní a výstupní soubor, jednotky ze vstupního souboru rozdělí do
skupin pomocí algoritmu quadtree, ke každé jednotce přidá informaci, do které
skupiny patří a jednotky s informacemi o skupinách vypíše do výstupního souboru.
Při programování počítejte s tím, že vstupních bodů můžou být desetitisíce.

## Vstup

Vstup je uložen ve formátu GeoJSON jako FeatureColection bodů. Každý bod má
nějaké properties, jejich hodnoty nás nezajímají, ale chceme je zachovat do
výstupního souboru.

## Výstup

Výstup bude uložen také ve formátu GeoJSON, ke každému bodu přibude property
`cluster_id`, která bude určovat, do které skupiny bod patří. Můžete
předpokládat, že tuto property žádný bod ve vstupním souboru nemá. `cluster_id`
musí být jedinečné pro každou skupinu.


## Další požadavky

Program by měl ošetřovat nekorektní vstupy a výjimky, v takovém případě by měl
vypsat chybovou hlášku a skončit s chybou (`exit(<cislo>)`, kde `cislo` je mezi
1 a 127).

## Doporučení
Předtím, než začnete programovat, rozmyslete se, jak by měl program fungovat a
pro ucelené části používejte funkce. Napište si kostru programu a pak
implementujte jednotlivé funkce, průběžně testujte, zda se chovají dle
očekávání.

