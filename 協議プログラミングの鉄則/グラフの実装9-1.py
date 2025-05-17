# N,M = map(int,input().split())

# edges = [list(map(int,input().split())) for _ in range(M)]

# G = [list() for i in range(N+1)]

# for a,b in edges:
#     G[a].append(b)
#     G[b].append(a)


N,M = map(int,input().split())

edges = [list(map(int,input().split())) for _ in range(N+1)]

# 
G = [list() for _ in range(N+1)]

for a,b in edges:
    G[a].append(b)
    G[b].append(a)

print(G)