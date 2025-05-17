T = list(input())
U = list(input())

ucount = 0
forcount = 0
syoki = True
while forcount - 1 < len(T) - len(U):
    
    for i in range(forcount, len(T)):


        if T[i] == U[ucount] or T[i] == "?":
            ucount += 1
            if syoki == True:
                forcount = i + 1
                syoki = False
            if ucount == len(U):
                print("Yes")
                exit()
        elif syoki == False:
                break

        else:
            ucount = 0
    syoki = True
    ucount = 0


print("No")