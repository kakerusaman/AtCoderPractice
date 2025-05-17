N,M = map(int,input().split())

A = list(map(int,input().split()))

def check():
    global A

    for i in range(M):
        if i+1 in A:
            continue
        else:
            return False
    return True


count = 0
while True:
    ans = check()
    if ans == True:
        A = A[:-1]
        count += 1
    else:
        print(count)
        exit()
