inputTestGeval = int(input("Hoeveel testgevallen wil je "))

if inputTestGeval < 50:
    teller = 0
    nList = []
    while teller < inputTestGeval :
        teller += 1
        inputGetal = int(input("Vul een natuurlijke getal in "))
        nList.append(inputGetal)

    som = 0
    for x in range (0, len(nList)):
        doorLopen = True
        while doorLopen:
            som += nList[x]
            abc = 0
            for y in range (len(str(som))):
                abc += int(str(som)[y])

            if abc == nList[x] :
                doorLopen = False
                print (som)
else:
    print ("Getal moet onder de 50 ")





