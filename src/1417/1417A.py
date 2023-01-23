t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    res, mi = 0, min(range(n), key=a.__getitem__)
    for i in range(n):
        if i != mi:
            res += (k - a[i]) // a[mi]
    print(res)
