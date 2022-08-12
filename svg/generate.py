from time import time
from random import randint

header = '<?xml version="1.0" encoding="UTF-8"?><svg id="a" xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 2351 2351">'
footer = "</svg>"

combinations = []

colors = [
    "#007c03",
    "#55e1ff",
    "#fcfe55",
    "#808200",
    "#fea800",
    "#2425e0",
    "#ac0051",
    "#12fe00",
    "#00ffa8",
    "#8a00ff",
    "#0042ff",
    "#00fe9c",
    "#fe00d2",
    "#fe0000",
    "#00c0ff",
]

reserved = [
    [3, 6, 2, 1, 5, 2, 0],
    [10, 8, 6, 13, 1, 8, 12],
    [13, 5, 8, 5, 11, 12, 4],
    [11, 5, 3, 7, 4, 6, 6],
    [11, 9, 11, 14, 6, 4, 13],
    [1, 3, 7, 7, 3, 9, 11]
]

def createmonster(ids=[randint(1, 15) for _ in range(7)]):
    j = 0

    randoms = ids
    color = colors[randoms[6]-1]
    while randoms in reserved:
        randoms = [randint(1, 15) for _ in range(7)]

    letters = ["a", "l", "h", "b", "e", "m"]

    content = ""

    for i in range(len(randoms)-1):
        with open(f"svg/{letters[i]}{randoms[i]}.svg", "r") as f:
            txt = f.read().replace(
                '<svg xmlns="http://www.w3.org/2000/svg" width="2351" height="2351">',
                "").replace("</svg>", "").replace("replace", color)

        content += txt

    return header + content + footer

def createmonsters(amount, outpath="monsters"):

    j = 0

    start = time()
    for j in range(amount): 
        randoms = [randint(1, 15) for _ in range(7)]
        if randoms in reserved and randoms in combinations:
            j -= 1
            continue
        
        combinations.append(randoms)
        with open(f"{outpath}/{j+1}_{randoms[0]}-{randoms[1]}-{randoms[2]}-{randoms[3]}-{randoms[4]}-{randoms[5]}-{randoms[6]}.svg", "w") as f:
            f.write(createmonster(randoms))

    print(time() - start)

createmonsters(10000)