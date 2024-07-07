n, m = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
l2r, r2l = [0] * n, [0] * n
for i in range(1, n):
    l2r[i] = max(0, a[i - 1] - a[i]) + l2r[i - 1]
    r2l[n - i - 1] = max(0, a[n - i] - a[n - i - 1]) + r2l[n - i]
for _ in range(m):
    s, t = (int(i) for i in input().split())
    if s <= t:
        res = l2r[t - 1] - l2r[s - 1]
    else:
        res = r2l[t - 1] - r2l[s - 1]
    print(res)
