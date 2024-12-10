N = int(input())

q = [0] * N
r = [0] * N
for i in range(N):
    q[i], r[i] = map(int, input().split())

query = int(input())
for i in range(query):
    t, d = map(int, input().split())
    t -= 1 #0種類目が存在するため-1
    diff = d - d // q[t] * q[t]
    if diff <= r[t]:
        print(d // q[t] * q[t] + r[t])
    else:
        print(d // q[t] * q[t] + r[t] + q[t])











"""



"""