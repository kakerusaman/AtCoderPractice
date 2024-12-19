def bubble_sort(a):
    for i in range(len(a) - 1):
        #列の先頭の要素を比較対象に選ぶ
        l = 0
        r = 1
    
        while r < len(a):
            if a[l] > a[r]:
                a[l], a[r] = a[r],a[l]

            l += 1
            r += 1