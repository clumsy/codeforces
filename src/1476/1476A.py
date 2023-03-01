t = int(input())
for _ in range(t):
    n = int(input())
    res = ["9"] * n
    for i in range(1, n):
        res[i] = str((i + 7) % 10)
    res = "".join(res)
    print(res)
