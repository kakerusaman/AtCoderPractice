N,M = map(int,input().split())

mlist = [list(map(int,input().split())) for i in range(M)]


tmpset = set()

coutn = 0

for i in range(M):
    if mlist[i][0] == mlist[i][1]:
        coutn += 1
        continue
    if (min(mlist[i][0],mlist[i][1]),max(mlist[i][0],mlist[i][1])) in tmpset:
        coutn += 1

    else:
        tmpset.add((min(mlist[i][0],mlist[i][1]),max(mlist[i][0],mlist[i][1])))
print(coutn)