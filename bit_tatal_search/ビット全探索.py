#ビット全探索はN個のものから、いくつか選ぶ方法を全列挙して調べ上げる。

def IntegerToVector(bit, N):
    S = []
    for i in range(N):
        if bit & (1 << i):
            S.append(i)
    return S


N = int(input())
W = int(input())
A = [int(input()) for _ in range(N)]

eist = False

for bit in range(1 << N):
    
    S = IntegerToVector(bit, N)

    sum = 0 

    for i in S:
        sum += A[i]
    
    if sum == W:
        exist = True


if exist:
    print("Yes")

else:
    print("No")