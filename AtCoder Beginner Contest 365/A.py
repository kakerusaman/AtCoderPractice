Y = int(input())

fornobai = Y % 100

if fornobai % 4 != 0:
    print(365)

elif fornobai % 4 == 0 and Y % 100 != 0:
    print(366)

elif Y % 100 == 0 and Y % 400 != 0:
    print(365)

else:
    print(366)