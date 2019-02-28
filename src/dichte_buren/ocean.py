import math
def gemiddelde(list):
    som = 0
    counter = 0
    for l in list:
        if not l == None:
            som += l
            counter += 1
    if som > 0 :
        return float(som)/float(counter)
    else:
        return print("Geen gemiddelde")



# print (gemiddelde([3, 7, 6, 11]))
# print (gemiddelde([3, None, None, 7, None, 6, 11]))
# print (gemiddelde([None, None, None, None, None]))

def gegevensbank(locatie):
    bestand = open(locatie)
    dict = {}
    for b in bestand:
        lol = b.split('\t')
        lol[14] = lol[14].strip()
        while lol.__contains__(''):
            lol[lol.index('')] = None
        dict[lol[1]] = lol[2],lol[3],lol[4],lol[5],lol[6],lol[7],lol[8],lol[9],lol[10],lol[11],lol[12],lol[13],lol[14]

    return dict
data = gegevensbank('ohi.txt')

# print (data['Belgium'])
# print (data['Netherlands'])
# print (data['France'])
# print (data['Monaco'])
# print (data['Jarvis Island'])
# print (data['Antarctica'])

def oceanHealthIndex(kuntstaat,data):
    if any(x == None for x in data[kuntstaat]):
        return gemiddelde(data[kuntstaat])
    getallen = data[kuntstaat]
    eerste = int(getallen[0]) + int(getallen[1]) + int(getallen[2])+ int(getallen[3]) + int(getallen[4])
    tweede = (int(getallen[5]) + int(getallen[6])) /2
    derde = int(getallen[7])
    vierde = (int(getallen[8]) + int(getallen[9])) /2
    vijfde = int(getallen[10])
    zesde = (int(getallen[11]) + int(getallen[12])) / 2
    antwoord = (eerste + tweede + derde + vierde + vijfde + zesde)/10
    return round(antwoord)

print(oceanHealthIndex('Belgium', data))
print(oceanHealthIndex('Netherlands', data))
print(oceanHealthIndex('France', data))
# print(oceanHealthIndex('Monaco', data))
# print(oceanHealthIndex('Jarvis Island', data))
#print(oceanHealthIndex('Antarctica', data))