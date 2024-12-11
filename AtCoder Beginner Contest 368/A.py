"""
N,K = map(int,input().split())
A = list(map(int,input().split()))
top = A[:-K] 
bottom = A[-K:] 
B = bottom + top 
print(*B)
"""


#これダメでした
N,K = map(int,input().split())
A = list(map(int,input().split()))

copy = []
if N %2 ==0:
    for i in range(K, N):
        tmp = A[i]
        copy.append(tmp)
else:
    for i in range(K-1, N):
        tmp = A[i]
        copy.append(tmp)

for i in range(len(copy)):
    A.pop()

for i in range(len(copy)):
    tmp = copy.pop()
    A.insert(0,tmp)

print(*A)