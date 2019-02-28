# Mike Yan
# s1098641
import sqlite3
import binascii

def openFile(text):
    f = open(text, "rb")
    hashObject = binascii.b2a_hex(f.read())
    f.close()
    vergelijkInDatabase(str(hashObject))


def toonPatroon(pattern):

    arrayPattern = [None, None, None, None, None, None, None, None, None]
    counter = 1
    for p in pattern:
        arrayPattern[int(p)] = counter
        counter += 1

    for p in range(0, 3):
        values = [None, None, None]
        for x in range(0, 3):
            values[x] = " " if arrayPattern[p * 3 + x] is None else str(arrayPattern[p * 3 + x])

        print('  -----  -----  -----')
        print('  | %s |  | %s |  | %s |  ' % (values[0], values[1], values[2]))
        print('  -----  -----  -----')

def vergelijkInDatabase(hashtext):
    connection = sqlite3.connect('AndroidLockScreenRainbow.sqlite')
    c = connection.cursor()

    # print(hashtext)
        #[1:] is nodig om de eerste character uit te halen zie print boven.
    c.execute("SELECT pattern FROM RainbowTable WHERE hash = " +hashtext[1:] + "")

    getalArray = []
    for g in c.fetchone()[0]:
        if str(g).isdigit():
            getalArray.append(g)
    toonPatroon(getalArray)



gesture1 = "gesture1.key"
gesture2 = "gesture2.key"
gesture3 = "gesture3.key"
gesture4 = "gesture4.key"
gesture5 = "gesture5.key"
gesture6 = "gesture6.key"
gesture7 = "gesture7.key"
gesture8 = "gesture8.key"
gesture9 = "gesture9.key"

openFile(gesture1)
print("======================================")
openFile(gesture2)
print("======================================")
openFile(gesture3)
print("======================================")
openFile(gesture4)
print("======================================")
openFile(gesture5)
print("======================================")
openFile(gesture6)
print("======================================")
openFile(gesture7)
print("======================================")
openFile(gesture8)
print("======================================")
openFile(gesture9)