N,M = map(int,input().split())

A = list(map(int,input().split()))
X = [] 

for i in range(N):
    X.append(list(map(int,input().split())))


ans = []

for i in range(N):
    for j in range(M):
        if i == 0:
            ans.append(X[i][j])
        
        else:
            ans[j] += X[i][j]
        
result = True

for i in range(M):
    if A[i] <= ans[i]:
        continue
    else:
        result = False
        break


if result == True:
    print("Yes")
else:
    print("No")
