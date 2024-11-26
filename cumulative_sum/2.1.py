"""
ある遊園地ではN日間にわたるイベントが開催され、i日目にはAi人が来場しました。
以下のQ個にこたえる質問を作成してください。
質問:L1日目からR1日目までの総来場者数は？
"""

N,Q = map(int,input().split())

A = list(map(int,input().split()))

L = [None] * Q
R = [None] * Q

for i in range(Q):
    L[i],R[i] = map(int,input().split())

total = [None] * (N+1)
total[0] = 0

for i in range(N):
    total[i+1] = total[i] + A[i]

for i in range(Q):
    print(total[R[i]] - total[L[i] -1])