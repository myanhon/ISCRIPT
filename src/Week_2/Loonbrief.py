randomSalaris = 645743
werknemer1 = 89329
werknemer2 = 34893
werknemer3 = 34398
werknemer4 = 23290
werknemer5 = 23923
werknemer6 = 23982
werknemer7 = 28493
werknemer8 = 29984
werknemer9 = 89033

werknemers = [randomSalaris, werknemer1, werknemer2, werknemer3, werknemer4, werknemer5, werknemer6, werknemer7, werknemer8, werknemer9]

totaalKosten = werknemers[0]
for w in range (1,len(werknemers)):
    totaalKosten += werknemers[w]
    print("werknemer #",w,"fluistert",totaalKosten)

totaalKosten -= werknemers[0]

print("Gemiddelde: €", float(totaalKosten) / (len(werknemers)-1))

