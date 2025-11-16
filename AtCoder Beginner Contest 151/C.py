N,M = map(int,input().split())

p = [None] * M
S = [None] * M

for i in range(M):
    p[i],S[i] = input().split()

wa = 0
ac = 0

genzainoatai = 0

flag = False

ans = []

for i in range(M):


    if genzainoatai != int(p[i]):
        genzainoatai = int(p[i])
        flag = False
    
    if S[i] == "AC" and flag == False:
        flag = True
        ac += 1
        ans.append(int(p[i]))


    elif S[i] == "WA" and flag == False:
        wa += 1

    

print(ac, wa, sep=" ")
    
