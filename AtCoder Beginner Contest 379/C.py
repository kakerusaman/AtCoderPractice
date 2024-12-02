N,M = map(int,input().split())

A = list(map(int,input().split()))
B = list(map(int,input().split()))

Nmasu = [0] * N

for i in A:
    Nmasu[i] = B[A.index(i)]

count = 0

sum = True
while sum == True:
    for i in range(N):
        if Nmasu[i] == 0:
            continue
        elif Nmasu[i] >= 1:
            if i == N:
                Nmasu[0] += 1
            else:
                Nmasu[i+1] += 1
            Nmasu[i] -= 1
            count += 1
        else:
            sum = False


print(count)

    