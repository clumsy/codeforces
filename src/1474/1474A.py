t = int(input())
for _ in range(t):
    n, b = int(input()), [int(c) for c in input()]
    res = [None] * n
    for i, e in enumerate(b):
        res[i] = 1 if i == 0 or res[i - 1] + b[i - 1] != 1 + b[i] else 0
    res = "".join(str(i) for i in res)
    print(res)
