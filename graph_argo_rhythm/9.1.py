N,M = map(int,input().split())

edges = [list(map(int,input().split())) for i in range(M)]

G= [list() for i in range(N+1)] #空の配列を作っている。

for a,b in edges:
    G[a].append(b)
    G[b].append(a)
print(edges)
print(G)

for i in range(1, N+1):
    output = ''
    output+= str(i)
    output+=':{'
    output+= ','.join(map(str,G[i]))
    output+='}'
    print(output)