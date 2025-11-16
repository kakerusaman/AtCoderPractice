X = int(input())
N = int(input())
WList = list(map(int,input().split()))
Q = int(input())

newWList = [[x, False] for x in WList]

for i in range(Q):
    tmp = int(input()) -1
    if newWList[tmp][1] == False:
        X += newWList[tmp][0]
        newWList[tmp][1] = True
    elif newWList[tmp][1] == True:
        X -= newWList[tmp][0]
        newWList[tmp][1] = False
    print(X)
    


    





