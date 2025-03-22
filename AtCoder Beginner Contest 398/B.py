A = list(map(int,input().split()))

zisyo = {}

for i in range(len(A)):
    if A[i] in zisyo:
        zisyo[A[i]] += 1
    else:
        zisyo[A[i]] = 1

three = 0
two = 0

for i in zisyo.values():
    if i >= 3:
        three += 1
    elif i >= 2:
        two += 1

if three >= 2:
    print("Yes")
elif three >= 1 and two >= 1:
    print("Yes")
else:
    print("No")
