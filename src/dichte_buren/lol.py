import math
def euclidischeAfstand(getallen1,getallen2):
    x1 = getallen1[0]
    y1 = getallen1[1]
    x2 = getallen2[0]
    y2 = getallen2[1]

    eerste = ((x1-x2)**2)
    tweede = ((y1-y2)**2)
    antwoord = math.sqrt(eerste+tweede)
    return antwoord

def dichtste(cel,dict,afstand=euclidischeAfstand):
    for key,value in dict.items():
        waarde =
    return

print(dichtste((0, 0), {(0, 6): 'B', (4, 7): 'D', (7, 5): 'E', (2, 3): 'A', (6, 1): 'C'}))