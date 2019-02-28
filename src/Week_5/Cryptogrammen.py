def antwoord(oplossing, lettersOplossing):
    antwoord = ""
    lengte_oplossing = len(oplossing)
    lengte_index = len(lettersOplossing)

    i = 0
    x = 0
    while(i < lengte_oplossing or x < lengte_index):
        char = oplossing[i]
        if(char == "?"):
            char = lettersOplossing[x]
            x += 1
        antwoord = antwoord + char
        i += 1

    return antwoord


def checkCharOpgave(char_opgave, opgave):
    index = []
    length = len(opgave)

    i = 0
    while(i < length):
        char = opgave[i]
        if(char == char_opgave):
            index.append(i)
        i += 1
    return index


def checkCharOplossing(mogelijke_indexen, oplossing):
    char = "?"
    length = len(mogelijke_indexen)

    i = 0
    while(i < length):
        index = mogelijke_indexen[i]
        letter = oplossing[index]
        if(not(letter == "?")):
            char = letter
        i += 1
    return char

def vraagtekenesOpgave(opgaveMetVraagtekens, opgave, oplossing):
    letters = []
    length_letters = len(opgaveMetVraagtekens)

    i = 0
    while(i < length_letters):
        char_opgave = opgaveMetVraagtekens[i]

        chars = checkCharOpgave(char_opgave, opgave)
        char_oplossing = checkCharOplossing(chars, oplossing)

        letters.append(char_oplossing)
        i += 1
    return letters

def vraagtekensOplossing(oplossing):
    vraagTekens = []
    length = len(oplossing)

    i = 0
    while(i < length):
        char = oplossing[i]
        if(char == "?"):
            vraagTekens.append(i)
        i += 1

    return vraagTekens


def lettersMetVraagtekenesOpgave(arrayVraagtekens, opgave):
    letters = []
    length = len(arrayVraagtekens)

    i = 0
    while(i < length):
        index = arrayVraagtekens[i]
        char = opgave[index].lower()
        letters.append(char)
        i += 1

    return letters

def cryptogram(opgave, oplossing):
    arrayVraagtekens = vraagtekensOplossing(oplossing)
    vraagTekensOpgave = lettersMetVraagtekenesOpgave(arrayVraagtekens, opgave)
    lettersKomenUitOpgave = vraagtekenesOpgave(vraagTekensOpgave, opgave, oplossing)
    cryptogram = antwoord(oplossing, lettersKomenUitOpgave)
    return cryptogram


opgave = 'Qmvrbwlf xwkd iopzlw vf zml pcwvfxzvyl.'
oplossing = 'Ch?ld??? ??ow fas??r ?n ??? ?p?i?gt?me.'
print(cryptogram(opgave, oplossing))

opgave = 'Zhp suxobpuw sbmtkopw Nxwkdnx.'
oplossing = '?h? p?n???a? ?rod?ces I???l??.'
print(cryptogram(opgave, oplossing))

opgave = 'Jujso ldmtq wyjqi tvadi ltek tq lads tw t wcqnej xjee.'
oplossing = '?v?ry ??ma? ?p??? ?bout h??f ?? ???? ?s ? ??ng?e c?l?.'
print(cryptogram(opgave, oplossing))

opgave = "V atult'a amrdd qvl zr nrbrqbrn zx v wumvl v medr vivx."
oplossing = "? ????k's ???l? ??n ?? ??t???ed ?y a hum?? ? ?i?? ?w??."
print(cryptogram(opgave, oplossing))


