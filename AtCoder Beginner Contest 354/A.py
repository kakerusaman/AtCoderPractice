H = int(input())

result = 1
count = 0
while True:
    if result > H:
        count += 1
        break
    else:
        count += 1
        result += 2 ** count

print(count)