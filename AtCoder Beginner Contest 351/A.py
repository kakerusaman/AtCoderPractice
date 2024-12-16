A = list(map(int, input().split()))
B = list(map(int, input().split()))

a_count = 0
b_count = 0

for i in A:
    a_count += i

for i in B:
    b_count += i

score_diff = a_count - b_count

if a_count == b_count:
    print(1)
else:
    print(score_diff + 1)