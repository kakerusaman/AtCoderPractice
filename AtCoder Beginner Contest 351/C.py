N = int(input())
A = list(map(int,input().split()))

answer_list = []

for i in range(N):
    #最初何も入っていないときには確実に追加する。
    if len(answer_list) == 0:
        answer_list.append(A[i])
        continue
    
    #Listの最後の値とAの値が同じだったら
    if answer_list[len(answer_list)-1] == A[i]:
        answer_list.pop()
        answer_list.append(A[i]+1)
        while True:
            if len(answer_list) >= 2:
                if answer_list[len(answer_list)-1] == answer_list[len(answer_list)-2]:
                    tmp = answer_list.pop()
                    answer_list.pop()
                    answer_list.append(tmp+1)
                else:
                    break
            else:
                break
    else:
        answer_list.append(A[i])
    


print(len(answer_list))
