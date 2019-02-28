def coordinaten(bestand):
    foto = open(bestand)
    list = []

    r = 0
    for f in foto:
        k = 0
        for i in f.strip():
            if i == '*':
                list.append((r,k))
            k += 1
        r += 1
    return list

def vergelijken(lijst1,lijst2):
    list = []

    for f in lijst1:
        if not lijst2.__contains__(f):
            list.append(f)
    return list

def afwijkingen(foto1,foto2):
    bestand1 = coordinaten(foto1)
    bestand2 = coordinaten(foto2)

    skuurt1 = vergelijken(bestand1,bestand2)
    skuurt2 = vergelijken(bestand2,bestand1)
    return skuurt1,skuurt2

def planeten():
    dict = {}

    return dict
# print(coordinaten('foto1.txt'))
# print(coordinaten('foto2.txt'))

vergelijken('foto1.txt', 'foto2.txt')
print(afwijkingen('foto1.txt', 'foto2.txt'))

