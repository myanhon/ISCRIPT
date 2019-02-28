def fen2grid(fen, karakter):
    grid = ""
    i = 0
    while i < len(fen):
        char = fen[i]

        if char == "/":
            grid += "\n"

        elif char.isdigit():
            c = 0
            while c < int(char):
                if karakter:
                    grid += karakter
                else:
                    grid += "*"
                c += 1
        else:
            grid += char
        i += 1
    return grid


def grid2fen(bord, char='*'):
    text = ""
    counter = 0
    for x in range(len(bord)):
        if bord[x] != "\n":
            if bord[x] == char:
                counter += 1
            else:
                if counter != 0:
                    text += str(counter)
                    counter = 0
                text += bord[x]
        else:
            if  counter != 0:
                text += str(counter)
                counter = 0
            text += "/"
    return text

print(fen2grid('rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR', '*'))
print(grid2fen(fen2grid('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR',"*")))