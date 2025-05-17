def dfs(pos,G,visited):
    visited[pos] = True
    for i in G[pos]:
        if visited == False:
            dfs(i,G,visited)

N,M = map(int,input().split())

edges = [list(map(int,input().split())) for _ in range(M)]

G = [list() for i in range(N+1)]

for a,b in edges:
    G[a].append(b)
    G[b].append(a)

visited = [False] * (N+1)

dfs(1,G,visited)

answer = True
for i in range(1,N+1):
    if visited[i] == False:
        answer = False


N,M = map(int,input().split())

edges = [list(map(int,input().split())) for i in range(M)]

G = [list() for i in range(N+1)]

for a,b in edges:
    G[a].append(b)
    G[b].append(a)

visited = [False] * (N+1)
