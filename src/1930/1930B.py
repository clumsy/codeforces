t = int(input())
for _ in range(t):
    n = int(input())
    res = [
        k
        for i, j in zip(reversed(range(2, n + 1, 2)), range(1, n - (n & 1), 2))
        for k in (i, j)
    ] + ([n] if n & 1 else [])
    print(*res)
