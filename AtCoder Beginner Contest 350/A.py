A = list(map(str,input()))

integer_num = []
for i in range(3,6):
    if i == "0":
        continue
    else:
        integer_num.append(A[i])

result = int("".join(integer_num))

if (result >= 1 and result <= 315) or (result >= 317 and result <= 349):
    print("Yes")
else:
    print("No")