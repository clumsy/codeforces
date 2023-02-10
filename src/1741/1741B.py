t = int(input())
for _ in range(t):
    n = int(input())
    mi = 1 + n // 2
    res = [-1] if n == 3 else list(range(mi, n + 1)) + list(range(1, mi))
    print(*res)
