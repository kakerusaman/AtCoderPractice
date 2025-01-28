N,T = map(int,input().split())

A = list(map(int,input().split()))

"""
各マスに対して、そのマスに印がつけられるターンを書き込む。このとき、ある列がビンゴを達成するターンはその列に含まれるマスに書かれた数の最大数に等しいです。
全ての列に対してその列が何ターン目にビンゴを達成するか求め、それらの最小値を答えればよい。
"""

mat = [[None] * N for i in range(N)]

for i in range(T):
    x,y = A[i] // N, A[i] % N