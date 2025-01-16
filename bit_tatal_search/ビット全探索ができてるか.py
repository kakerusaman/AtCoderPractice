n = 5
for bit in range(1<<n):
    S = [i for i in range(n) if bit & (1 << i)]

    print(F"{bit}:{{{', '.join(map(str, S))}}}")