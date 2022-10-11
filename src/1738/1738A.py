t = int(input())
for _ in range(t):
    n = int(input())
    a = (int(i) for i in input().split())
    b = (int(i) for i in input().split())
    f, c = [], []
    for i, (a, b) in enumerate(zip(a, b)):
        (f if a == 0 else c).append(b)
    f, c = sorted(f), sorted(c)
    f, c = (c, f) if len(f) > len(c) or (len(f) == len(c) and c[0] < f[0]) else (f, c)
    res = (
        sum(c[: len(c) - len(f)])
        + 2 * sum(c[len(c) - len(f) :])
        + 2 * sum(f)
        - (f[0] if len(f) == len(c) else 0)
    )
    print(res)
