#index()メソッド。リスト内に指定した要素が何番目にあるかを返してくれる。
#例えばindex(3)とすると、リスト内の3が何番目にあるかを返してくれる。[1,2,3,4,5]なら2が返ってくる。

"""
N = int(input())
A = list(map(int,input().split()))

ans = []

for i in range(N):
    if A[i] == i+1:#正しい位置に存在しているかどうかで判定している。A[0]番目は1番目なため、A[0]が1であれば正しい位置に存在している。
        continue
    index = A.index(i+1)
    A[i],A[index] = A[index],A[i]
    ans.append((i+1,index+1))
    
print(len(ans))
for i in ans:
    print(*i)    
"""
#上記無理だった
#これができなかった理由はindexメソッドを使っているからでした。indexメソッドもループ処理が行われている為、計算量が増えてしまい、TLEになってしまう。

"""

N = int(input())

A = list(map(int,input().split()))

count = 0
Nlist = [0] * N
answer_list = []
for i in range(N):
    Nlist[i] = i+1

for i in range(N):
    if A[i] == Nlist[i]:
        continue

    else:
        count +=1
        tmp = Nlist[i]

"""




n = int(input())
a = list(map(int, input().split()))
n2index = [0] * n
for i in range(n):
    a[i] -= 1
    n2index[a[i]] = i

result = []
for i in range(n):
    if a[i] != i:
        t = n2index[i]
        n2index[a[i]] = t
        n2index[i] = i
        a[t] = a[i]
        a[i] = i
        result.append((i + 1, t + 1))

print(len(result))
for i in range(len(result)):
    print(*result[i])
