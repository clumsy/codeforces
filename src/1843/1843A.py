t = int(input())
for _ in range(t):
    n, a = int(input()), sorted(int(i) for i in input().split())
    res = 0
    for i in range(1, n // 2 + 1):
        res = max(res, sum(a[-i:]) - sum(a[:i]))
    print(res)
