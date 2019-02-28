# Mike Yan
# s1098641
eersteInputCoordinaat = input("Vult het eerste coordinaat ")
tweedeInputCoordinaat = input("Vult het tweede coordinaat ")

eersteInputLetter = ord(eersteInputCoordinaat[0])
eersteInputCijfer = int(eersteInputCoordinaat[1])

tweedeInputLetter = ord(tweedeInputCoordinaat[0])
tweedeInputCijfer = int(tweedeInputCoordinaat[1])


if (abs(eersteInputLetter - tweedeInputLetter) == 1) and (abs(eersteInputCijfer - tweedeInputCijfer)==2) or \
                (abs(eersteInputLetter - tweedeInputLetter) == 2) and (abs(eersteInputCijfer - tweedeInputCijfer)==1) :
    print("het paard kan springen van", eersteInputCoordinaat, " naar ", tweedeInputCoordinaat)
else:
    print("het paard kan niet springen van", eersteInputCoordinaat, " naar ", tweedeInputCoordinaat)


