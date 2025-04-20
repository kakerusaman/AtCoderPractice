N = int(input())
S = input()
T = input()

count = 0


for i in range(N):
    if S[i] == T[i]:
        continue
    else:
        count += 1

print(count)