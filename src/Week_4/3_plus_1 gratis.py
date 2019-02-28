# Mike Yan
# s1098641
def samen(prijzenLijst):
    getal = 0.0

    lengte = int(len(prijzenLijst) / (3 + 1))
    prijzenLijst.sort()
    for p in prijzenLijst:
        if(lengte !=0):
            lengte -= 1
        else:
            getal += p
    return round(getal,2)

def groeperen(prijzen):
    prijzen.sort()
    prijzen = prijzen[::-1]
    prijs = []
    nieuweprijzen = []
    for p in prijzen:
        prijs.append(p)
        if (len(prijs) == 4):
            nieuweprijzen.append(prijs)
            prijs = []
    nieuweprijzen.append(prijs)
    return nieuweprijzen

def gegroepeerd(prijzen):
    prijzen = groeperen(prijzen)
    getal = 0.0
    for p in prijzen:
            for l in range(len(p)):
                if(l < 3):
                    getal += p[l]
    return round(getal, 2)

def winst(prijzenlijst):
    return (round(float(samen(prijzenlijst)) - float(gegroepeerd(prijzenlijst)),2))



prijzen = [3.23, 5.32, 8.23, 2.23, 9.98, 7.43, 6.43, 8.23, 4.23]
print(samen(prijzen))
print(groeperen(prijzen))
print(gegroepeerd(prijzen))
print(winst(prijzen))
