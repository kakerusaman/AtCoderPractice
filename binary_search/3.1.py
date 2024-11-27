N,X = map(int,input().split())

A = list(map(int,input().split()))

def search(x, A):
    L = 0
    R = N - 1
    while L <= R:
        M = (L + R) // 2
        if x < A[M]:
            R = M - 1
        if x == A[M]:
            return M
        if x > A[M]:
            R = M + 1
    return -1

Answer = search(X,A)

print(Answer + 1)