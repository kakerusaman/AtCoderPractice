S = input()

tmp = []

for i in S:
    if i == "2":
        tmp.append(2)

print("".join(map(str,tmp)))