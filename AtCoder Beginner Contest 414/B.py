N = int(input())

answer = []
count = 0

for i in range(N):
    tmp = list(input().split())

    for j in range(int(tmp[1])):
        answer.append(tmp[0])
        count += 1
        if count >= 101:
            print("Too Long")
            exit()

if count < 101:
    print("".join(answer))
else:
    print("Too Long")