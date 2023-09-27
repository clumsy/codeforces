t = int(input())
for _ in range(t):
    n, b = int(input()), (int(i) for i in input().split())
    # mm mm mm m
    # mm ff mm f
    # mm ff m f
    res = k = u = 0
    for i in b:
        if i == 2:
            k += u
            u = 0
        else:
            u += 1
        res = max(res, (k // 2 + 1 if k else 0) + u)
    print(res)
