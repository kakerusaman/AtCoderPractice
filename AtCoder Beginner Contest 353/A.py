N = int(input())

H = list(map(int,input().split()))

max_value = H[0]
max_index = 0

flag = False

for index,value in enumerate(H):
    if  max_value < value:
        max_value = value
        max_index = index
        flag = True
        break


if flag == True:
    print(max_index + 1)
else:
    print(-1)
