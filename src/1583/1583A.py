def is_composite(n):
    return any(n == i * (n // i) for i in range(2, n // 2))


t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    s, res = sum(a), set(i + 1 for i in range(n))
    if not is_composite(s):
        res.remove(next(i + 1 for i, a_i in enumerate(a) if a_i & 1 == 1))
    print(len(res)), print(*res)
