N,K = map(int,input().split())
A = list(map(int,input().split()))
top = A[:-K] 
bottom = A[-K:] 
B = bottom + top 
print(*B)