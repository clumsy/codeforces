t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = sorted(int(i) for i in input().split())
    res, s = n, 0
    for i in range(n):
        if i > 0 and a[i] - a[i - 1] > k:
            s = i
        res = min(res, n - (i + 1 - s))
    print(res)
