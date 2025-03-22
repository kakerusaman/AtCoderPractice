N = int(input())
A = list(map(int,input().split()))

zisyo = {}

for i in range(len(A)):
    if A[i] in zisyo:
        zisyo[A[i]][0] += 1
    else:
        zisyo[A[i]] = [1,i]

maxvalue = 0

tmpindex = 0

valueflag = False

for key, value in zisyo.items():
    # 重複していないか
    if value[0] == 1:
        valueflag = True
        if key > maxvalue:
            maxvalue = key
            tmpindex = value[1]


if valueflag == True:
    print(tmpindex+1)
else:
    print(-1)
