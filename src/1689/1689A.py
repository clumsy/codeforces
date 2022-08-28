t = int(input())
for _ in range(t):
    n, m, k = (int(i) for i in input().split())
    a, b = sorted(input()), sorted(input())
    res, w = [], k
    while a and b:
        if a > b or not w:
            a, b, w = b, a, k
        res += a[0]
        a = a[1:]
        w -= 1
    print("".join(res))
