X = list(map(str,input()))

check = True

while X[-1] == "0":
    if X[-1] == "0": #-1で末尾の取得
        X.pop() #popは後ろから
    if X[-1] == ".":
        X.pop()
        check = False
        break
result = "".join(X)


if check == True:
    print(float(result))
else:
    print(int(result))




"""
https://qiita.com/oyoshi0022/items/07ea473d7476593b9662
stripを使用した実装方法

def getString():
    return input()


def main():
    X = getString()

    print(X.rstrip("0").rstrip("."))


if __name__ == "__main__":
    main()
"""