H,W = map(int,input().split())

S1,S2 = map(int,input().split())

C = []
C.append(list("0"))
takahasi = (S1,S2)
for i in range(H):
    C.append(list(input()))

X = list(input())

for i in X:
    if i == "U" and C[takahasi[0] - 1,takahasi[1]] != "#":
        takahasi = takahasi[0] - 1, takahasi[1]
    
    elif i == "L" and

