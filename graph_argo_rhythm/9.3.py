N,M = map(int,input().split())
edges = [list(map(int,input().split())) for i in range(M)]

G = [list() for i in range(N+1)]

for a,b in edges:
    G[a].append(b)
    G[b].append(a)

