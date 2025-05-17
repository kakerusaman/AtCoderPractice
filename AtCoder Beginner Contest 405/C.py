N = int(input())
A = list(map(int,input().split()))

S = sum(A)
Ss = sum(i**2 for i in A)

ans = (S**2 - Ss) // 2
print(ans)