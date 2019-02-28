
def prijzen(file, **argumenten):
    file = open(file, 'r')
    doorGaan = False

    for rij in file:
        rij = rij.split(';')

        rows = {'prijs': rij[0], 'discipline': rij[1], 'jaar': rij[2], 'laureaat': rij[3], 'motivering': rij[4]}
        rows['laureaten'] = rows['laureaat'].split(",")

        for obj in sorted(argumenten):
            if obj == "nationaliteit":
                nationaliteit = []
                laureaten = rows['laureaat'].split(",")
                i = 0
                matches = []
                match = False
                for laureaat in laureaten:
                    nationaliteit.append(laureaat.partition('(')[-1].rpartition(')')[0])

                for nat in nationaliteit:
                    if nat.lower() == argumenten[obj].lower():
                        matches.append(rows['laureaten'][i])
                        match = True
                    i += 1
                if match:
                    doorGaan = True
                else:
                    doorGaan = False
                    break

            elif obj == "laureaten":
                if len(rows[obj]) is not argumenten[obj]:
                    doorGaan = False
                    break

            elif obj == "motivering":
                motivering = rows['motivering'].split(" ")
                i = 0
                for woord in motivering:
                    motivering[i] = woord.replace('\n', '').lower()
                    i += 1
                if argumenten[obj].lower() not in motivering:
                    doorGaan = False
                    break

            elif obj in rows:
                if str(argumenten[obj]).lower() == rows[obj].lower():
                    doorGaan = True
                else:
                    doorGaan = False
                    break

        if doorGaan:
            regel = rows['prijs'] + ' voor de ' + rows['discipline'] + ' (' + rows['jaar'] + '): '
            i = 0
            for obj in rows['laureaten']:
                regel += obj
                if len(rows['laureaten']) - 1 > i:
                    regel += ', '
                    i += 1
            print(regel)



prijzen('prijzen.csv', prijs='nobelprijs', jaar=1994)
print("==========================================================")
prijzen('prijzen.csv', prijs='nobelprijs', discipline='wiskunde')
print("==========================================================")
prijzen('prijzen.csv', nationaliteit='bel')
print("==========================================================")
prijzen('prijzen.csv', discipline='scheikunde', laureaten=3)
print("==========================================================")
prijzen('prijzen.csv', motivering='röntgen', discipline='natuurkunde', nationaliteit='GB')


