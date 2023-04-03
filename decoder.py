key = {
    "W": "V",
    "E": "D",
    "K": "C",
    "U": "T",
    "B": "S",
    "D": "R",
    "O": "Z",
    "P": "I",
    "J": "U",
    "F": "G",
    "Z": "A",
    "A": "Q",
    "Y": "O",
    "Q": "N",
    "I": "M",
    "C": "E",
    "L": "P",
}


def decode(code):
    replaced_chars = [key.get(char, char) for char in code]
    return "".join(replaced_chars)


cypher = "AJCJC | LZPD-LDYFDZIIPQF | ZEWPBYD ICCUPQFB | ICBBZFC PQBUDJKUYD YD ICQUYD"

with open("support-cryptogram.txt", "w") as file:
    file.write(decode(cypher))
