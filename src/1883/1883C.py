t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    res, e = k, 0
    for i in a:
        if k == 4 and n > 1:
            e += i & 1 == 0
            res = min(res, max(0, 2 - e), (k - (i % k)) % k)
        else:
            res = min(res, (k - (i % k)) % k)
    print(res)
