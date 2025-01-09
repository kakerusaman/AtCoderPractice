N = int(input())

A = list(map(int,input().split()))

count = 0
for i in range(len(A)):
    if i == 0:
        continue
    if i == len(A)-1:
        break

    if A[i-1] == A[i+1]:
        count += 1

print(count)