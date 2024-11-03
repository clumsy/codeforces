t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    x, y = max(x, y), min(x, y)
    res = 1
    while x & 1 == y & 1:
        x >>= 1
        y >>= 1
        res <<= 1
    print(res)
