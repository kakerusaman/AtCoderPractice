#挿入ソートは手に持ったトランプの並び替え方に例えられる手法。配列をソート済みの部分とみソート部分に分けて考え、未ソート部分の要素をソート部分の
#しかるべき位置に挿入する平均計算時間・最悪計算時間はともにO(n2)

def insertion_sort(a):
    for i in range(len(a) -1):
        j  = i + 1

        while i >= 0:
            if a[j] < a[i]:
                a[i],a[j] = a[j], a[i]

                i -= 1
                j -= 1
            else:
                break