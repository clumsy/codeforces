t = int(input())
for _ in range(t):
    n = int(input())
    b, s = (input() for _ in range(2))
    free = need = 0
    for i, j in zip(b, s):
        if i == "1" and j == "0":
            free += 1
        elif i == "0" and j == "1":
            need += 1
    reus = min(free, need)
    res = free + need - reus
    print(res)
