S = input()

counter = 0

tmp = []

for i in range(len(S)):
    #counterを初期化する
    if counter == 2:
        counter = 0
        tmp.clear()
    
    if S[i] == "#":
        counter += 1
        tmp.append(i+1)
    
    if counter == 2:
        print(*tmp, sep=',')

    
    

