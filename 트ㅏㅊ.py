import sys
sys.stdin = open('./input.txt', 'r')
input = sys.stdin.read
qwerty = {
    "`": "0",
    "1": "`",
    "2": "1",
    "3": "2",
    "4": "3",
    "5": "4",
    "6": "5",
    "7": "6",
    "8": "7",
    "9": "8",
    "0": "9",
    "-": "0",
    "=": "-",
    "q": "]",
    "w": "q",
    "e": "w",
    "r": "e",
    "t": "r",
    "y": "t",
    "u": "y",
    "i": "u",
    "o": "i",
    "p": "o",
    "[": "p",
    "]": "[",
    "\\": "]",
    "a": "'",
    "s": "a",
    "d": "s",
    "f": "d",
    "g": "f",
    "h": "g",
    "j": "h",
    "k": "j",
    "l": "k",
    ";": "l",
    "'": ";",
    "z": "/",
    "x": "z",
    "c": "x",
    "v": "c",
    "b": "v",
    "n": "b",
    "m": "n",
    ",": "m",
    ".": ",",
    "/": "."
}

res = []

for i in input().lower():
    if i in qwerty:
        res.append(qwerty[i].upper())
    else:
        res.append(i)
print(''.join(res))