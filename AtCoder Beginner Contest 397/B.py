S = list(input())

ans = []

count = 0

for i in range(len(S)):
    if i % 2 == 0 and S[i] == "i":
        ans.append("i")
    elif i % 2 == 1 and S[i] == "o":
        ans.append("o")
    elif i % 2 == 0 and S[i] == "o":
        ans.append("i")
        ans.append("o")
        count += 1
    elif i % 2 == 1 and S[i] == "i":
        ans.append("o")
        ans.append("i")
        count += 1

if len(ans) % 2 == 1:
    ans.append("o")
    count += 1


print(count)