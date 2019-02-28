# Mike Yan
# s1098641
import math
invoer = 4.2
graden = invoer * 180 / math.pi
minuten = (graden - math.floor(graden)) * 60
seconden =  (minuten - math.floor(minuten)) * 60

print(math.floor(graden),"Graden",math.floor(minuten),"Minuten",math.floor(seconden),"Seconden")
