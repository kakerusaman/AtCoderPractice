N,M = map(int,input().split())

def f(i):
    return N ** i

def siguma(func,M):
    resurt = 0
    for i in range(M + 1):
        resurt += func(i)
    return resurt

sum = siguma(f, M)

if sum <= 10 ** 9:
    print(sum)
else:
    print("inf")


