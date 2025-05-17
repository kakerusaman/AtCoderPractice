N = int(input())

S = []
T = []
Tsyapu = 0
ans = 0
# Tのリストと判定する。
def check():
    global ans
    global S
    global T
    global Tsyapu
    count = 0
    for i in range(N):
        for j in range(N):
            if S[i][j] == "#" and T[i][j] == "#":
                count += 1
    
    ans = max(ans, count)

def rotate():
    global S
    rotated = [list(row) for row in zip(*S[::-1])]
    S = rotated



for i in range(N):
    S.append(list(input()))
for i in range(N):
    tmp = list(input())
    Tsyapu += tmp.count("#")
    T.append(tmp)



check()

# ４回測定を行う。
for i in range(3):
    # Sのリストを90ド回転させる
    rotate()
    check()








# Sのリストを回転させる
