import random
# Mike Yan
# s1098641
def gebeuren_samen(m, n):
    testen = [0] * m
    gelijk = False
    x = 0
    while(x < n):
        waarde = random.randrange(m)
        testen[waarde] += 1
        if testen[waarde] > 1:
            gelijk = True
        x = x + 1
    return gelijk

def schat_kans(m, n, i):
    getalGelijk = 0.0
    getal = 0
    while(getal < i):
        if(gebeuren_samen(m, n)):
            getalGelijk = getalGelijk + 1
        getal = getal + 1
    return getalGelijk / i


print(gebeuren_samen(6, 3))
print(gebeuren_samen(6, 3))
print(schat_kans(6, 2, 10000))
print(schat_kans(365, 23, 10000))

