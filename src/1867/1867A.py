t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    m = {
        e: i + 1
        for i, e in enumerate(sorted(range(n), key=a.__getitem__, reverse=True))
    }
    res = [m[i] for i in range(n)]
    print(*res)
