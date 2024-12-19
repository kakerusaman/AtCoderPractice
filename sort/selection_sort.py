def selection_sort(a):
    for i in range(len(a)):
        min_idx = i

        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        
        #発見した最小値の未ソート部分の先頭に移す

        if i != min_idx:
            a[i], a[min_idx] = a[min_idx],a[i]