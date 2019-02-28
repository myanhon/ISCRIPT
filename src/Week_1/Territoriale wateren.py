# Mike Yan
# s1098641
import math
x1 = float(input("Voer het getal van x1 in"))
y1 = float(input("Voer het getal van y1 in"))
x2 = float(input("Voer het getal van x2 in"))
y2 = float(input("Voer het getal van y2 in"))
x3 = float(input("Voer het getal van x3 in"))
y3 = float(input("Voer het getal van y3 in"))
zeemijl = 1852
zone = ""
u = (((x3 - x1) * (x2 - x1))+((y3 - y1) * (y2-y1))) / (((x2 - x1)**2) + ((y2-y1)**2))
Xv = x1 + u*(x2-x1)
Yv = y1 + u*(y2 -y1)
a = math.sqrt((((Xv - x3)**2)+ ((Yv - y3)**2)))

if((a* zeemijl) <= (12*zeemijl)):
    zone = "territoriale wateren"
elif ((a* zeemijl) <=(24*zeemijl)):
    zone ="aansluitende zone"
elif((a*zeemijl) <=(200*zeemijl)):
    zone = " exclusieve economische zone"
else:
    zone = " internationale wateren"

print("Voertpunt: ",Xv,Yv)
print("Afstand",a)
print(zone)
