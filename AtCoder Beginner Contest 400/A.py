A = int(input())

sum = 400 / A

if sum.is_integer():
    print(int(sum))
    exit()

print(-1)