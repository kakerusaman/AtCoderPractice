N,K,M = map(int,input().split())

A = list(map(int,input().split()))

Alist = sum(A)

tmp = Alist



for i in range(K):

    if i == 0:
        if Alist / N >= M:
            print(i)
            exit()

    tmp += 1

    if tmp / N >= M:
        print(i + 1)
        exit()



print(-1)
