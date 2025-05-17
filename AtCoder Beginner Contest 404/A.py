S = input()

char = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i in range(len(char)):
    if char[i] in S:
        continue
    else:
        print(char[i])
        exit()
