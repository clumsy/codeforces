t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    c = [int(i) for i in input().split()]
    res = [None] * n
    for i in range(n):
        res[i] = next(
            k
            for k in (a[i], b[i], c[i])
            if k != res[(i + 1) % n] and k != res[(i - 1) % n]
        )
    print(*res)
