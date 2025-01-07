N,A = map(int,input().split())

T = list(map(int,input().split()))


cnt = 0
for i in range(N):
    if i == 0:
        cnt += T[i]
    
    elif cnt < T[i]:
        cnt += T[i] - cnt
    


    cnt += A

    print(cnt)
