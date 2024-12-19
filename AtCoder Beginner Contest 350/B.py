N,Q = map(int,input().split())

T = list(map(int,input().split()))


#歯の生えているリストを作成する。生えている1。生えていない０
tooth_list = [1] * N


for i in T:
    if tooth_list[i-1] == 1:
        tooth_list[i-1] = 0
    else:
        tooth_list[i-1] = 1

tooth_count = 0

for i in range(N):
    if tooth_list[i-1] == 1:
        tooth_count += 1

print(tooth_count)