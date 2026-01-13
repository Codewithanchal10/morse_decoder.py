morse = {
    "._": "A", "_...": "B", "_._.": "C", "_..": "D", ".": "E",
    ".._.": "F", "__.": "G", "....": "H", "..": "I", ".___": "J",
    "_._": "K", "._..": "L", "__": "M", "_.": "N", "___": "O",
    ".__.": "P", "__._": "Q", "._.": "R", "...": "S", "_": "T",
    ".._": "U", "..._": "V", ".__": "W", "_.._": "X", "_.__": "Y",
    "__..": "Z"
}

encrypted = input()

results = []

def solve(pos, word):
    if pos == len(encrypted):
        results.append(word)
        return

    for code in morse:
        length = len(code)
        if encrypted[pos:pos + length] == code:
            solve(pos + length, word + morse[code])

solve(0, "")

results.sort()

for r in results:
    print(r)