
S,T=input().split()
ans="No"
for i in range(1,len(S)):
    K=[""]*i
    for j in range(len(S)):
        K[j%i]+=S[j]
    if T in K:
        ans="Yes"
print(ans)