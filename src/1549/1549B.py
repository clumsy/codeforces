t = int(input())
for _ in range(t):
    n = int(input())
    e = [int(i) for i in input()]
    g = (int(i) for i in input())
    res = 0
    for i, c in enumerate(g):
        if c == 1:
            if i > 0 and e[i - 1] == 1:
                res += 1
            elif e[i] == 0:
                e[i] = -1
                res += 1
            elif i < n - 1 and e[i + 1] == 1:
                e[i + 1] = -1
                res += 1
    print(res)
