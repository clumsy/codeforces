t = int(input())
for _ in range(t):
    n, a = int(input()), sorted(int(i) for i in input().split())
    res = 0
    for i in reversed(range(n)):
        res = max(res, (n - i) * a[i])
    print(res)
