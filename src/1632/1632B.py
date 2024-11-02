t = int(input())
for _ in range(t):
    n = int(input())
    p = 1
    while 1 << p < n:
        p += 1
    res = list(range(1, 1 << (p - 1))) + [0] + list(range(1 << (p - 1), n))
    print(*res)
