N,M = map(int,input().split())

H = list(map(int,input().split()))

counter = M
count = 0

for i in range(N):
    counter -= H[i]
    count += 1
    if counter <= -1:
        count -=1
        break
    elif counter == 0:
         break
print(count)

