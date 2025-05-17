N,M,Q = map(int,input().split())


kara = []
zisyo = {}

for i in range(Q):
    a,b,c = map(int,input().split())
    if a == 1:

        zisyo[b] = kara.append(c)
    elif a == 2:

        zisyo[b] = kara.append("all")

    else:
        if b in zisyo and zisyo[b] is not None:
            if "all" in zisyo[b]:
                print("Yes")
            elif c in zisyo[b]:
                print("Yes")
            else:
                print("No")
        else:
            print("No")


