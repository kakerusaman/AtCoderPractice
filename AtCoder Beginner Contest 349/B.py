S = list(input())
sum = []
tmp = []
for i in range(len(S)):
    if S[i] in sum:
        None
    else:
        tmp.append(S.count(S[i]))
        sum.append(S[i])



flag = True
for i in range(len(tmp)):
    if tmp.count(tmp[i]) != 2:
        flag = False
    
if flag:
    print("Yes")
else:
    print("No")