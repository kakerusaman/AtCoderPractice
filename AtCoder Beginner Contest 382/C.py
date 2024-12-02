N,M = map(int,input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

search = [0] * len(N)

#一番最初の値は入れておく
search[0] = A[0]

for i in range(N-1):
    search[i+1] = min(A[i+1],A[i])

