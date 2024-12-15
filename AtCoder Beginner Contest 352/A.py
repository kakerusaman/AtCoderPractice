N,X,Y,Z = map(int,input().split())

train_flag = False #下り列車
answer_flag = False

if X < Y:
    train_flag = True #上り列車

if train_flag == True:
    for i in range(X,Y):
        if i == Z:
            answer_flag = True
else:
    for i in range(X,Y,-1):
        if i == Z:
            answer_flag = True

if answer_flag == True:
    print("Yes")
else:
    print("No")
