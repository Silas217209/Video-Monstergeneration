from random import randint

header = '<?xml version="1.0" encoding="UTF-8"?><svg id="a" xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 2351 2351">'
footer = "</svg>"


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

randoms = [randint(1, 15) for _ in range(7)]
color = colors[randoms[6]-1]

letters = ["a", "l", "h", "b", "e", "m"]

content = ""

for i in range(len(randoms)-1):
    with open(f"svg/{letters[i]}{randoms[i]}.svg", "r") as f:
        txt = f.read().replace(
            '<svg xmlns="http://www.w3.org/2000/svg" width="2351" height="2351">',
            "").replace("</svg>", "").replace("replace", color)

    content += txt

with open(f"monsters/{randoms[0]}-{randoms[1]}-{randoms[2]}-{randoms[3]}-{randoms[4]}-{randoms[5]}-{randoms[6]}.svg", "w") as f:
    f.write(header + content + footer)