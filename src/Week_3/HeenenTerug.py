# Mike Yan
# s1098641
def decodeer(bericht, kolommen):
    decodeerBericht = ""
    lijstBerichten = list(bericht[0 + i:kolommen + i] for i in range(0, len(bericht), kolommen))

    for b in range(len(lijstBerichten)):
        if not b % 2 == 0:
            lijstBerichten[b] = lijstBerichten[b][::-1]


    for kolom in range(kolommen):
        for rij in range(len(lijstBerichten)):
            decodeerBericht += lijstBerichten[rij][kolom]

    return decodeerBericht


print(decodeer("aoesifibolwkrdexeioayngoxxfhtslhtlx", 5))