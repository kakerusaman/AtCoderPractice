A,B = list(map(int,input().split()))

ans = []
#小さいほうを考える
if A < B:
    for i in range(B):
        ans.append(str(A))
else:
    for i in range(A):
        ans.append(str(B))

print("".join(ans))