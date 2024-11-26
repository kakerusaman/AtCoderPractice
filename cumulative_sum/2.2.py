"""
ある会社ではD日間にわたってイベントが開催され、N人が出席します。
参加者i(i=1,2,3...N)はLi日目からRi日目まで出席する予定です。
各日の出席者数を出力するプログラムを作成してください。
"""
D = int(input())
N = int(input())

L = [None] * N
R = [None] * N

for i in range(N):
    L[i],R[i] = map(int, input().split())

total = [0] * (D+1)
total[0] = 0

#わいオリジナル計算量の問題でもしかしたら無理かも
#そしたら調べてみよう！
count = 0
while count != N:
    for j in range(N):
        for i in range(L[j],R[j] + 1):
            total[i] += 1
        count += 1  

for i in range(D):
    print(total[i+1])
