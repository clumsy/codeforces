t = int(input())
for _ in range(t):
    n, x = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    if a[-1] < x:
        a.append(x + (x - a[-1]))
    res = min(a[0], x)
    for i in range(1, len(a)):
        cur = a[i] - a[i - 1]
        if a[i] > x:
            cur = min(cur, 2 * (x - a[i - 1]))
        res = max(res, cur)
    print(res)
