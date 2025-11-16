H,B = map(int,input().split())

if H == B:
    print(0)
elif H < B:
    print(0)
else:
    tmp = H - B
    print(tmp)