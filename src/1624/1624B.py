t = int(input())
for _ in range(t):
    a, b, c = (int(i) for i in input().split())
    res = "NO"
    d, r = divmod(b - (c - b), a)
    if d > 0 and r == 0:
        res = "YES"
    d, r = divmod(a + (c - a) / 2, b)
    if d > 0 and r == 0:
        res = "YES"
    d, r = divmod(b + (b - a), c)
    if d > 0 and r == 0:
        res = "YES"
    print(res)
