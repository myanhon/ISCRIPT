import math

invoer = (int(input("voer je getal in ")))


a = 0
test = 0.25 * invoer
while a < (0.25 * invoer):
    a += 1
    b = a
    c = 0
    while(a+b+c) <= invoer:
        c = math.sqrt(math.pow(a,2) + math.pow(b,2))
        if(a + b  + c) == invoer:
            print (a,b,int(c))

        b += 1