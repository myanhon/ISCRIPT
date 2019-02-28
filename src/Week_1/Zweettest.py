# Mike Yan
# s1098641
leeftijdMaand = int(input("Voer het leeftijd van de patient"))
mmol = int(input("Voer het invoer voor mmol"))

if (mmol >= 60) and (leeftijdMaand > 6):
    print("CF is waarschijnlijk")
elif (mmol >= 30 <= 59) or (leeftijdMaand >= 6 and mmol >= 40 <= 59):
    print("CF is mogelijk")
elif (mmol <= 29)  or (leeftijdMaand > 6 and mmol <= 39):
   print("CF is Hoogst onwaarschijnlijk")