N,M = map(int,input().split())

B = list(map(int,input().split()))
W = list(map(int,input().split()))

B.sort(reverse=True)
W.sort(reverse=True)

tmp = 0

#今現在の値を保持する
count = 0

#Bよりも小さくならないように判定する。
bcount = 0
wcount = 0

#二回ダメだったらもうダメでしょ
twoflag = 0


for i in range(N):
    tmp += B[i]
    if i < M and W[i] >= 0:
        tmp += W[i]

    count = max(tmp, count)

print(count)


    
        

