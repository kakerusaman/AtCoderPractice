N = int(input())
A = list(int,input().split())
B = list(int,input().split())

dp = [None] * (N+1)
dp[1] = 0
dp[2] = A[0]

for i in range(3, N+1):
    dp[i] = min(dp[i-1]+A[i-2], dp[i-2]+B[i-3])

answer = []
place = N

while True:
    answer.append(place)
    if place == 1:
        break

    if dp[place-1] + A[place-2] == dp[place]:
        place = place -1
    else:
        place = place -2

answer.reverse

answer2 = [str(i) for i in answer]
print(len(answer))
print(" ".join(answer2))