N = int(input())

S = [None] * N

count = 0

for i in range(N):
    S[i] = input()

    if S[i] == "Takahashi":
        count +=1

print(count)