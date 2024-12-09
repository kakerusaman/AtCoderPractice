#置き方を全部試す。

def calc(a, b, x, y):
    res = 0
    for i, s_i in enumerate(S):
        for j, s_ij in enumerate(s_i):
            if s_ij == "." and (abs(a - i) + abs(b - j) <= D or abs(x - i) + abs(y - j) <= D):
                res += 1
    return res


# H, W, D の値を入力から取得
H, W, D = map(int, input().split())


S = [input().split() for _ in range(H)]

ans = 0
print(S)
for x1 in range(H):
    for y1 in range(W):
        if S[x1][y1] == "#":
            continue
        for x2 in range(H):
            for y2 in range(W):
                if (x1,y1) == (x2,y2) or S[x2][y2] == "#":
                    continue
                ans = max(ans,calc(x1,y1, x2, y2))

