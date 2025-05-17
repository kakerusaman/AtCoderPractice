N,K = map(int,input().split())

S = 2

tmptmp = 0
tmp = 0
sum = 0
syoki = True

for i in range(N - K):
    if syoki:
        tmptmp = 1
        tmp = S
        sum = S+tmptmp
        syoki = False
        continue

    tmptmp = tmp
    tmp = sum
    sum = tmp + tmptmp

MOD = 10**9

print(sum % MOD)



    

