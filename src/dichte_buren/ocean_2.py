def gemiddelde(list):
    som = 0
    counter = 0
    for l in list:
        if not l == None:
            som += l
            counter += 1
    if som > 0:
        return  float(som) / float(counter)





print(gemiddelde([3, 7, 6, 11]))
print(gemiddelde([3, None, None, 7, None, 6, 11]))
print(gemiddelde([None, None, None, None, None]))
