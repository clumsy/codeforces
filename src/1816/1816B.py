t = int(input())
for _ in range(t):
    n = int(input())
    res = [
        [i for f, s in zip(range(2 * n, n, -2), range(2, n + 1, 2)) for i in (f, s)],
        [i for f, s in zip(range(1, n, 2), range(n + 1, 2 * n + 1, 2)) for i in (f, s)],
    ]
    for r in res:
        print(*r)
