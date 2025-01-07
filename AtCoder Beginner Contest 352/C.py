N = int(input())

kyozin = []

for i in range(N):
    kyozin.append(list(map(int,input().split())))


answer = 0

for i in range(N):
    answer += kyozin[i][0]

answer += kyozin[len(kyozin)-1][1] - kyozin[len(kyozin)-1][0]

print(answer)
