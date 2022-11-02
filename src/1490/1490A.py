t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res = 0
    for i in range(n - 1):
        # we can also insert a single middle element to make it dense
        ma, mi = max(a[i], a[i + 1]), min(a[i], a[i + 1])
        while ma / mi > 2:
            res += 1
            ma = (ma + 1) // 2
    print(res)
