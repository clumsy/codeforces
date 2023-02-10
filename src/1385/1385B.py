t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res, found = [], [False] * (n + 1)
    for i in a:
        if not found[i]:
            found[i] = True
            res.append(i)
    print(*res)
