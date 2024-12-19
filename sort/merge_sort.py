#配列を昇順に並べる。
def merge_sort(a):
    if len(a) == 1:
        return
    
    #配列を二つに分ける
    m = len(a) // 2
    x = a[:m]
    y = a[m:]

    #分割とマージを再帰的に行う。最終的に一つの要素まで分割された段階からマージ開始

    merge_sort(x)
    merge_sort(y)
    merge(x,y,a)

def merge(x,y,a):
    #x,yのインデックス
    i = 0
    j = 0


    # x, yの先頭の要素を比較し、小さい要素から順にaにセットしていく
    while i < len(x) or j < len(y):
        # xの要素を全て追加済みの場合、y[j]をセットする
        if i == len(x):
            a[i+j] = y[j]
            j += 1
        # yの要素を全て追加済みの場合、x[i]をセットする
        elif j == len(y):
            a[i+j] = x[i]
            i += 1
        # x[i]がy[j]以下の場合、x[i]をセットする
        elif x[i] <= y[j]:
            a[i+j] = x[i]
            i += 1
        # y[j]がx[i]より小さい場合、y[j]をセットする
        else:
            a[i+j] = y[j]
            j += 1