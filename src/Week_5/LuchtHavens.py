from math import *

def afstand(vliegveld, vliegveld2, luchtHavens):
    R = 6372.795
    b1 = float(luchtHavens[vliegveld][0])
    b2 = float(luchtHavens[vliegveld2][0])
    l1 = float(luchtHavens[vliegveld][1])
    l2 = float(luchtHavens[vliegveld2][1])

    b1, b2, l1, l2 = map(radians, [b1, b2, l1, l2])
    dl = l1 - l2

    f_boven = (((cos(b2) * sin(dl)) ** 2) + (((cos(b1) * sin(b2)) - (sin(b1) * cos(b2) * cos(dl))) ** 2))
    f_boven_wortel = sqrt(f_boven)
    f_onder = (sin(b1) * sin(b2) + cos(b1) * cos(b2) * cos(dl))
    resultaat = R * atan2(f_boven_wortel, f_onder)

    return resultaat


def tussenlanding(vliegveld, vliegveld2, luchthavens, afstandTussenlanding):

    vliegveld3 = " "
    max_afstand = 2 * afstandTussenlanding

    if(afstand(vliegveld, vliegveld2, luchthavens) > afstandTussenlanding):
        for lv in luchthavens:
            afstand1 = afstand(vliegveld, lv, luchthavens)
            afstand2 = afstand(lv, vliegveld2, luchthavens)
            if afstand1 < afstandTussenlanding & afstandTussenlanding > afstand2:
                totale_afstand = afstand1 + afstand2
                if totale_afstand < max_afstand:
                    max_afstand = totale_afstand
                    vliegveld3 = lv

        if(max_afstand != 2 * afstandTussenlanding):
            return vliegveld3


def leesLuchthavens(txtBestand):
    bestand = open(txtBestand, 'r')
    luchtHavensArray = {}
    i = 0
    for rij in bestand:
        if i > 0:
            rij = rij.split("	")
            rij[4] = rij[4].replace('\n', "")
            x = 0
            locatie = []
            for obj in rij:
                if x > 0:
                    locatie.append(obj)
                x += 1
            luchtHavensArray[rij[0].partition('[')[-1].rpartition(']')[0]] = locatie
        i += 1

    return luchtHavensArray



luchthavens = leesLuchthavens('luchthavens.txt')
print (luchthavens)
print (luchthavens['ADK'])
print (luchthavens['DCA'])
print (luchthavens['4OM'])
print (afstand('P60', 'MSN', luchthavens))
print (afstand('ADK', 'DCA', luchthavens))
print (tussenlanding('ADK', 'DCA', luchthavens, 4000))


