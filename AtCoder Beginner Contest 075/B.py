H,W = map(int,input().split())

A = [None] * H


for i in range(H):
    A[i] = list(input())


count = 0
for i in range(H):
    for j in range(W):
        if A[i][j] == "#":
            continue

        if 0 < i and 0 < j:
            print()
