N,T = map(int,input().split())

A = list(map(int,input().split()))

"""
各マスに対して、そのマスに印がつけられるターンを書き込む。このとき、ある列がビンゴを達成するターンはその列に含まれるマスに書かれた数の最大数に等しいです。
全ての列に対してその列が何ターン目にビンゴを達成するか求め、それらの最小値を答えればよい。
"""

#列３ 行３ 斜め２の順番で値を入れていく
ans = [0] * (N * 2 +2)

for i in range(T):
    