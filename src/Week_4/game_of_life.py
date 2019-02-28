# Mike Yan
# s1098641
def toonGeneratie(generatie):

    for x in range(len(generatie)):
        rij = " "
        for y in generatie[x]:
            if(y):
                rij += ("X ")
            else:
                rij += ("O ")
        print(rij)

def volgendeGeneratie(generatie):
    volgende = [[False] * len(generatie[0]) for _ in range(len(generatie))]
    for x in range(len(generatie)):
        for y in range (len(generatie[x])):
            buren = aantalBuren(generatie,x,y)
            if(buren == 2) | (buren == 3):
                volgende[x][y] = generatie[x][y]
            if (buren == 3) & (not generatie[x][y]):
                volgende[x][y] = True
            if(buren == 1):
                volgende[x][y] = False
            if(buren >= 4):
                volgende[x][y] = False

    return volgende

def aantalBuren(generatie,xpos,ypos):
    buren = 0
    beginX = -1
    eindeX = 2
    beginY = -1
    eindeY = 2
    if(xpos == 0):
        beginX += 1
    if (ypos == 0):
        beginY += 1
    if (xpos == len(generatie) -1):
        eindeX -= 1
    if (ypos == len(generatie[xpos]) -1):
        eindeY -=1
    for x in range(beginX, eindeX):
        for y in range(beginY,eindeY):
            if(xpos + x == xpos):
                if(ypos + y == ypos):
                    continue
            if (generatie[xpos + x][ypos + y]):
                buren += 1
    return buren



generatie = [[True] + [False] * 7 for _ in range(6)]
toonGeneratie(generatie)
print(aantalBuren(generatie, 0, 0))
print(aantalBuren(generatie, 1, 1))
print(aantalBuren(generatie, 2, 2))
volgende = volgendeGeneratie(generatie)
toonGeneratie(volgende)
print()
volgende = volgendeGeneratie(volgende)
toonGeneratie(volgende)
print()
volgende = volgendeGeneratie(volgende)
toonGeneratie(volgende)
print()
volgende = volgendeGeneratie(volgende)
toonGeneratie(volgende)

