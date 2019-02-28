invoer = (int(input("Voer het aantal wachtwoord die jij wilt!")))

teller = 0

while teller < invoer:
    teller += 1
    wachtwoord = input("voer wachtwoord in: ")
    count = 0
    if any(c.islower() for c in wachtwoord):
        count = count + 1

    if any(c.isupper() for c in wachtwoord):
        count = count +1

    if any(c.isdigit() for c in wachtwoord):
        count = count +1

    chars = set('!@#%^&*_$+=,')
    if any((c in chars) for c in wachtwoord):
        count = count + 1

    print ("wachtwoord: "+ wachtwoord)

    if len(wachtwoord)>8 and count ==4:
        print("Dit wachtwoord: sterk")

    if count == 1:
        print("Dit wachtwoord: Zwak")

    if count == 2 or count == 3:
        print("Dit wachtwoord: maatig")
