import math
def hoofdsteden(locatie):
   bestand = open(locatie)
   dict = {}

   for b in bestand:
        staat = b.split(',')
        dict[staat[1].strip()]=(staat[0])
   return dict




hoofdstad = hoofdsteden('hoofdsteden.txt')
print (hoofdstad['TX'])
print (hoofdstad['NE'])



def coordinaten(locatie):
    bestand = open(locatie)
    dict = {}

    for b in bestand:
        staat = b.split(',')
        dict[staat[0] + ","+ staat[1]]=(float(staat[2]),float(staat[3]))
    return dict


coordinaat = coordinaten('steden.txt')
print (coordinaat['Dalhart,TX'])

def grootcirkelafstand(stad1,stad2):
    b1= math.radians(stad1[0])
    l1 = math.radians(stad1[1])
    b2 = math.radians(stad2[0])
    l2 = math.radians(stad2[1])
    r = 6371
    eerste = math.sin(b1)* math.sin(b2)
    tweede = math.cos(b1) * math.cos(b2) * math.cos(l1 - l2)
    return r * math.acos(eerste + tweede)

print (grootcirkelafstand((36.1173, -102.6024), (30.352, -97.7151))) # Dalhart,TX <-> Austin,TX

def dichteBuren(staat,hoofdstad,coordinaat):
    coordinaat1 = coordinaat[staat]
    key = staat.split(',')
    coordinaat2 = coordinaat[hoofdstad[key[1]]+','+key[1]]
    afstand = grootcirkelafstand(coordinaat1,coordinaat2)
    list = []

    for k in hoofdstad:
        if not k == key[1]:
            coordinaat2 = coordinaat[hoofdstad[k] + ',' + k]
            afstand2 = grootcirkelafstand(coordinaat1, coordinaat2)
            if afstand >= afstand2:
               list.append(hoofdstad[k] + ',' + k)
    return list

print(dichteBuren('Dalhart,TX', hoofdstad, coordinaat))