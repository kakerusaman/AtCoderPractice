import math

N = int(input())

tmp = []
mannnaka = math.ceil(N / 2)

flag = False
for i in range(1,N + 1):
    if mannnaka > i:
        tmp.append("-")
    elif mannnaka == i:
        tmp.append("=")
        if N % 2 == 0:
            flag = True
    elif mannnaka < i:
        if flag:
            tmp.append("=")
            flag = False
        else:
            tmp.append("-")


print("".join(tmp))

