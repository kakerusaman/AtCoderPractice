S = list(input())

for i in range(len(S)):
    if i == 0 and S[i] != "<":
        continue
    else:
        
        print("No")
        exit()

    if i == len(S)-1 and S[i] != ">":
        print("No")
        exit()
    else:
        pass

    if S[i] == "=":
        continue
    else:
        print("No")
        exit()
    
print("Yes")

    