S = list(input())
T = list(input())

answer_list = []

count = 0

for index, value in enumerate(T):
    if S[count] == value:
        answer_list.append(index+1)
        count += 1
        continue
        


print(*answer_list)