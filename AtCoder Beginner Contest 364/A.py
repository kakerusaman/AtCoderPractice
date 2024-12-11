N = int(input())

S = [None] * N

for i in range(N):
    S[i] = input()


check = False
for i in range(N):
    if i == N-1:
        check = True
        break
    if S[i] == S[i+1]:
        if S[i] == "salty":
            continue
        elif i < N-2:
            check = False
            break
        else:
            Check = True

if check == False:
    print("No")
else:
    print("Yes")