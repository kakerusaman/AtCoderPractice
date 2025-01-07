N = int(input())

A = list(map(int,input().split()))

tmp =[]

result = False

for i in range(N):
    if A[i] % 2 == 0:
        tmp.append(A[i])

if len(tmp) != 0:
    for i in range(len(tmp)):
        if tmp[i] % 3 == 0 or tmp[i] % 5 == 0:
            result = True
        else:
            result = False
            break
        
if result == True:
    print("APPROVED")
else:
    print("DENIED")
