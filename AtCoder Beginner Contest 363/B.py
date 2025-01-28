N,T,P = map(int,input().split())

L = list(map(int,input().split()))

daynum = 0

while True:
    peoplecount = 0
    for i in range(N):
        if L[i] >= T:
            peoplecount += 1
            L[i] += 1
        else:
            L[i] += 1
    
    if peoplecount >= P:
        print(daynum)
        break
    daynum += 1














