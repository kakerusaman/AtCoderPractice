N = int(input())

P = list(map(int,input().split()))

ans = [list() for _ in range(1,N+1)]

r = 1

for i in range(N):
    for j in range(N):

        hoge = max(P[j], P[i])

        if hoge > P[i]:
            r += 1

    print(r)
    r = 1


    
