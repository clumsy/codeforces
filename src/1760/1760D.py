t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res, d = 0, -1
    for i in range(1, n):
        if a[i] > a[i - 1]:
            res += d < 0
            d = 1
        elif a[i] < a[i - 1]:
            res += d > 0
            d = -1
    res += d < 0
    res = "YES" if res == 1 else "NO"
    print(res)
