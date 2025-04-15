N = int(input())

S = []

for i in range(N):
    S.append(input())

#エラーの回数をカウント
error = 0

#ログイン常態か判定
login = False

for i in range(N):
    if S[i] == "login":
        login = True
    elif S[i] == "logout":
        login = False
    elif S[i] == "public":
        continue
    elif S[i] == "private":
        if login == False:
            error += 1
    

print(error)