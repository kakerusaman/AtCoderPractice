import time

N = int(input())
A = list(map(int,input().split()))
index = 0
count = 0
flag = True
start = time.perf_counter()
while flag:
    for i in range(index,N):
        if A[index] <= A[i] /2:
            count += 1
        
    if index == N -1:
        flag = False

    index += 1
end  = time.perf_counter()
print(count)

print(f"実行時間: {end - start:.6f} 秒")