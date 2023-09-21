t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    order = sorted(range(n), key=a.__getitem__, reverse=True)
    res = [0] * (n + 1)
    for i in range(n):
        res[order[i] + 1] = ((-1) ** (i & 1)) * ((i + 2) // 2)
    s = sum(
        2 * abs(res[i] - res[0]) * a[i - 1] if i > 0 else 0 for i, e in enumerate(res)
    )
    print(s)
    print(*res)
