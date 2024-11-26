import time
N = 100 
M = 100 
L = 100 
start_time = time.time() 
for i in range(N): 
    for j in range(M): 
        for k in range(L): 
            # 何らかの処理（ここでは空の処理） 
            pass 
end_time = time.time()
elapsed_time = end_time - start_time 
print(f"Elapsed time: {elapsed_time} seconds")