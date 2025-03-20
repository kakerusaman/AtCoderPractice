W,B = map(int,input().split())

tmpW = W
tmpB = B


mozi = "wbwbwwbwbwbw"

for i in range(W+B):
    #文字列の一番目から始めるとき
    if i == "w":
        if tmpW == 0:
            print("No")
            exit()
        else:
            tmpW -=1
    elif i == "b":
        if tmpB == 0:
            print("No")
            exit()
        else:
            tmpB -= 1
