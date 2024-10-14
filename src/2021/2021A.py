t = int(input())
for _ in range(t):
    n, a = int(input()), sorted(int(i) for i in input().split())
    res, ma = a[:2]
    for i in a[2:]:
        if i > ma:
            res = (res + ma) // 2
            ma = i
        else:
            res = (res + i) // 2
    res = (res + ma) // 2
    print(res)
