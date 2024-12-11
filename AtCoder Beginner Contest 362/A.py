Red, Green, Blue = map(int,input().split())

pen_name = input()

if pen_name == "Red":
    if Green > Blue:
        print(Blue)
    else:
        print(Green)

elif pen_name == "Green":
    if Red > Blue:
        print(Blue)
    else:
        print(Red)

elif pen_name == "Blue":
    if Red > Green:
        print(Green)
    else:
        print(Red)
