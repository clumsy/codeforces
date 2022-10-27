t = int(input())
for _ in range(t):
    w, h, n = (int(i) for i in input().split())
    res, wh = 1, w * h
    while wh % 2 == 0:
        res *= 2
        wh /= 2
    res = "YES" if res >= n else "NO"
    print(res)
