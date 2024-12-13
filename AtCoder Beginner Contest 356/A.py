N,L,R = map(int,input().split())

A = []

for i in range(1, N+1):
    A.append(i)

if L == R:
    print(*A)
else:
    print("totyuudesu")