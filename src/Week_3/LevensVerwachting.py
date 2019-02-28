# Mike Yan
# s1098641
def levensverwachting(geslacht,roker,sport,alcohol,fastfood):
    leeftijd = 70

    if(geslacht == "vrouw"):
        leeftijd += 4

    if (roker):
        leeftijd -= 5
    else:
        leeftijd += 5
    if(sport > 0):
        leeftijd += sport
    else:
        leeftijd -= 3

    if (alcohol == 0):
        leeftijd += 2
    elif(alcohol > 7):
        leeftijd -= ((alcohol - 7) * 0.5)

    if not(fastfood):
        leeftijd += 3

    return leeftijd


print (levensverwachting(geslacht='man', roker=True, sport=2, alcohol=10, fastfood=True))
print (levensverwachting(geslacht='man', roker=True, sport=5, alcohol=5, fastfood=True))
print (levensverwachting(geslacht='vrouw', roker=False, sport=5, alcohol=0, fastfood=False))
print (levensverwachting(geslacht='vrouw', roker=False, sport=3, alcohol=14, fastfood=True))
print (levensverwachting(geslacht='man', roker=False, sport=4, alcohol=4, fastfood=False))


