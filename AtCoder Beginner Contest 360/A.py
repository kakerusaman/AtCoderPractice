S = list(input())

check = False

for i in range(len(S)):
    if S[i] == "R" and i == 0:
        check = True
    elif i == 1 and S[i+1] == "M":
        check = True

if check == True:
    print("Yes")
else:
    print("No")
