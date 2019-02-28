import math


def euclidischeAfstand(getallen1, getallen2):
    x1 = getallen1[0]
    y1 = getallen1[1]
    x2 = getallen2[0]
    y2 = getallen2[1]
    eerste = ((x1 - x2) ** 2)
    tweede = ((y1 - y2) ** 2)
    antwoord = math.sqrt(eerste + tweede)
    return antwoord


def manhattanAfstand(getallen1, getallen2):
    x1 = getallen1[0]
    x2 = getallen2[0]
    y1 = getallen1[1]
    y2 = getallen2[1]
    eerste = (x1 - x2)
    tweede = (y1 - y2)
    antwoord = float(abs(eerste + tweede))
    return antwoord


def schaakbordAfstand(getallen1, getallen2):
    x1 = getallen1[0]
    x2 = getallen2[0]
    y1 = getallen1[1]
    y2 = getallen2[1]
    eerste = (x1 - x2)
    tweede = (y1 - y2)
    antwoord = max(float(abs(eerste)), float(abs((tweede))))
    return antwoord


def posities(bestand):
    gun = open(bestand)
    dict = {}
    crisis = []

    for index, b in enumerate(gun):
        crisis.append(b)
        for index1, a in enumerate(b):
            if a.isalpha():
                lijst = (index, index1)
                dict[lijst] = a
    return len(crisis), len(crisis), dict


def dichtste(cel, dict, afstand=euclidischeAfstand):
    array = []
    for key, value in dict.items():
        waarde = (afstand(cel, key), value)
        array.append(waarde)
    kleinsteWaarde = min(array)
    print(kleinsteWaarde)

    # print(kleinsteWaarde)

    return kleinsteWaarde[1]


# print(euclidischeAfstand((0, 0), (3, 4)))
# print(manhattanAfstand((0, 0), (3, 4)))
# print(schaakbordAfstand((0, 0), (3, 4)))
print(posities('ziekenhuizen.txt'))
print(dichtste((0, 0), {(0, 6): 'B', (4, 7): 'D', (7, 5): 'E', (2, 3): 'A', (6, 1): 'C'}))
print(dichtste((8, 8), {(0, 6): 'B', (4, 7): 'D', (7, 5): 'E', (2, 3): 'A', (6, 1): 'C'}, afstand=manhattanAfstand))
