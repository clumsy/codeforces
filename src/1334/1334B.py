t = int(input())
for _ in range(t):
    n, x = (int(i) for i in input().split())
    a = sorted((int(i) for i in input().split()), reverse=True)
    res, s = n, 0
    for i in range(n):
        if (s + a[i]) / (i + 1) < x:
            res = i
            break
        s += a[i]
    print(res)
