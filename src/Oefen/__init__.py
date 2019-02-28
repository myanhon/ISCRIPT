import random,sys,os
#
# Numbers Strings Lists tuples Dictionaries


#List je kan van alles mee doen

# grocery_list = ['Juice','Tomatoes','Potatoes','Bananas']
#
# print('first item',grocery_list[0])
#
# print(grocery_list[1:3])
#
# other_events = {'wash car','pick up kids','cash check'}
#
# to_do_list = [grocery_list,other_events]
#
# print(to_do_list[0][3])
#
# grocery_list.append('aiemel')
#
# grocery_list.insert(2,'hoi')
#
# print(grocery_list)
#
# grocery_list.sort()
#
# print(grocery_list)
#
# grocery_list.reverse()
#
# print(grocery_list)
#
# del grocery_list[4]
#
# print(grocery_list)
#
# print(len(grocery_list))
# print(max(grocery_list))
# print(min(grocery_list))



# #tuples kan je de waarde niet veranderen
#
# pi_tuple = (3,1,4,1,5,9)
#
# new_tuple = list(pi_tuple)
# new_list = tuple(new_tuple)
#
# new_tuple.append(6)
# print(new_tuple)
# print(new_list)

#Dictionaries elke waarde is uniek    -> je kan ze niet joinen
#linker kant is de key
# super_villians = {'Fiidler':'Isaac Bowin',
#                   'Captain Cold': 'Leonard Snart',
#                   'Weather Wizard': ' Mark Mardon'
#                   }
#
# print(super_villians['Captain Cold'])
# print(super_villians.keys())
# print(super_villians.values())

# for x in range(0,10):
#  print(" "+ str(x))


# grocery_list = ['Juice','Tomatoes','Potatoes','Bananas']
#
# for y in grocery_list:
#     if y == 'Tomatoes':
#         print (y)

# numb_list = [[1,2,3,4,5],[10,20,30,40,50],[100,200,300,400,500]]
#
# for row in range(0,3):
#     for index in range(0,5):
#         print(numb_list[row][index])

random_num = random.randrange(0,40)

# while(random_num != 15):
#     print (random_num)
#

# i = 0;
#
# while(i <= 20):
#     if(i%2 == 0):
#         print(i)
#     elif(i == 9):
#         break
#     else:
#         i += 1
#         continue
#
#     i+=1


# def addNumber(fNum,lNum):
#     sumNum = fNum + lNum
#     return sumNum
#
#
# String = (addNumber(5,5))

# print("Wat is je naam")
#
# name = sys.stdin.readline()
#
# print(name)

# long_string = "I will suck your dick"
#
# #print 1 tot en met de vijfde karakters
# print(long_string[0:5])
#
# #print de laatste 5 karakters
# print(long_string[-5:])
#
# # 0 tot en met max printen
# print(long_string[:-5])
#
# print(long_string[:5])
#
# print("%s gaat %c %d" % ("Shaban",'D',9999))
#
# print(long_string.capitalize())
#
# print(long_string.find("will"))
#
#
# print(long_string.strip())
#
# print(str(long_string.isalpha()) + " alle karakters string")
#
# print(str(long_string.isalnum()) + " is alleen getallen")
#
# quote_lost = long_string.split()
#
# for q in quote_lost:
#     print (q.isalpha())
#
# print(quote_lost)

# test_file = open("text,tx")

class Animal:
    __name = ""
    __lengte = None
    __leeftijd = 0

    def __init__(self, name,lengte):
        self.__name = name
        self.__lengte = lengte

    def set_name(self,name):
        self.__name = name

    def get__name(self):
        return self.__name

    def set_lengte(self, lengte):
        self.__lengte = lengte

    def get_lengte(self):
        return self.__lengte

    def get_type(self):
        print("Animal")

    def toString(selfs):
        return "{} is {} lengte".format(selfs.__name,selfs.__lengte)

cat = Animal("Rover",5)

print (cat.toString())
