t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res, cnt = 0, sum(1 for i in range(n) if a[i] != i + 1)
    while cnt > 0:
        for i in range(0 if res & 1 == 0 else 1, n - 1, 2):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                cnt -= a[i] == i + 1
                cnt += a[i + 1] == i + 1
                cnt -= a[i + 1] == i + 2
                cnt += a[i] == i + 2
        res += 1
    print(res)
