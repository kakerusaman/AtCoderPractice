N,D = map(int,input().split())

T = [None] * N
L = [None] * N

for i in range(N):
    T[i],L[i] = list(map(int,input().split()))

tmp = 0

for i in range(1,D+1):
    tmp = 0
    for j in range(N):
        num = i+ L[j]
        if tmp < T[j] * num:
            tmp = T[j] * num
    print(tmp)

