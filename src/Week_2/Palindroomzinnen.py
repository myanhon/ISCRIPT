invoer = input("voer aantal zinnen")

teller = 0
while teller < invoer:
    teller+=1
    zin = input()

    zin = zin.lower()
    zin = zin.replace(" ","")
    zin = zin.replace(".","")
    zin = zin.replace(",","")

    zin2 = zin[::-1]

    if zin == zin2:
        print("ja, het is palindroomzin")
    else:
        print("nee het is geen palindroomzin")