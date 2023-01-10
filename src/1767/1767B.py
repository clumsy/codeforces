t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res, a = next(a), sorted(a)
    for e in a:
        res += max(0, (e + 1 - res) // 2)
    print(res)
