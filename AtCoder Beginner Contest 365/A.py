Y = int(input())

multiple = Y % 100

if multiple % 4 != 0:
    print(365)

elif multiple % 4 == 0 and Y % 100 != 0:
    print(366)

elif Y % 100 == 0 and Y % 400 != 0:
    print(365)

else:
    print(366)