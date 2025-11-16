N,L,R = map(int,input().split())

watch = []

for i in range(N):
    watch.append(list(map(int,input().split())))

count = 0

for i in range(N):
    if watch[i][0] <= L:
        if watch[i][1] >= R:
            count += 1


print(count)
