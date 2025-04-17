N,K = map(int,input().split())

A = list(map(int,input().split()))


def search(X):

    if A[N-1] < X:
        return -1

    ng = 0 -1
    ok = N
    while ok - ng > 1:
        M = (ok+ng) // 2

        if A[M] > X:
            ok = M
        
        elif A[M] == X:
            return M
        
        elif A[M] < X:
            ng = M
        
    return M


ans = search(K)

print(ans)