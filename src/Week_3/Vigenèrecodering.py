# Mike Yan
# s1098641
def codeer(Zin, Sleutel):
    bericht = ""
    sleutelCounter= 0
    #isupper checkt de hoofdletters
    for z in Zin:
        if (z.isupper()):
            z = int(ord(z) - 65) # 65 = A
            s = int(ord(Sleutel[sleutelCounter]) - 65) # 65 = A
            v = (z + s) % 26
            bericht += chr( 65 + v)  # 65 = A
        else:
            bericht += z
            if (sleutelCounter == (len(Sleutel) - 1)):
                sleutelCounter = 0
            else:
                sleutelCounter += 1
    return bericht

def decodeer(Zin, Sleutel):
    bericht = ""
    sleutelCounter = 0
    # isupper checkt de hoofdletters
    for z in Zin:
        if (z.isupper()):
            v = int(ord(z) - 65) # 65 = A
            s = int(ord(Sleutel[sleutelCounter]) - 65) # 65 = A
            z = (v - s) % 26
            bericht += chr(ord('A') + z)
        else:
            bericht += z
        if(sleutelCounter == (len(Sleutel)- 1)):
            sleutelCounter = 0
        else:
            sleutelCounter += 1
    return bericht

print(codeer('NOBODY EXPECTS THE SPANISH INQUISITION!', 'CIRCUS'))
print(decodeer('PWSQXQ MORYUVA VBW AGCHAUP KHIWQJKNAQV!', 'CIRCUS'))
print(codeer('OH SHUT UP! AND GO AND CHANGE YOUR ARMOUR!', 'ARTHUR'))
print(decodeer('OY ZBLT NW! AEW AF RGK THRGNY YFNY RRDHBL!', 'ARTHUR'))





