"""
質問に対して素数かどうか判定する。
素数とは「１」と自分自身以外の約数を持たない自然数。
例えば23を素数か判定するときに2～22の中に割り切れる数がない場合は素数。
"""

def isPrime(x):
    LIMIT = int(x ** 0.5)
    for i in range(2, LIMIT+1):
        if x % i == 0:
            return False
    return True


Q = int(input())

X = [None] * Q

for i in range(Q):
    X[i] = int(input())



for i in range(Q):
    Answer = isPrime(X[i])
    if Answer == True:
        print("Yes")
    else:
        print("No")