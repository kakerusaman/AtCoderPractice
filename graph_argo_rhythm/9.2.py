def dfs(pos, G, visited):
    visited[pos] = True
    for i in G[pos]:
        if visited[i] == False:
            dfs(i,G,visited)


N,M = map(int,input().split())

edges = [list(map(int,input().split())) for i in range(M)]

#隣接リストの作成
G = [list() for i in range(N+1)]
for a,b in edges:
    G[a].append(b)
    G[b].append(a)

visited = [False] * (N-1)
dfs(1,G ,visited)

answer = True
for i in range(1,N+1):
    if visited[i] == False:
        answer = False
    
if answer == True:
    print("The graph is connected.")
else:
    print("The graph is not connected.")