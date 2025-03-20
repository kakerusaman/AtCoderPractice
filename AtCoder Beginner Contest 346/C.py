N,K = map(int,input().split())

A = list(map(int,input().split()))

tmp = {}

for i in A:
    tmp[i] = 0

ans = 0

for i in range(1,K+1):
    if i in tmp:
        continue
    else:
        ans += i

print(ans)
