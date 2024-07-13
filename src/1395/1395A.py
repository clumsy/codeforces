t = int(input())
for _ in range(t):
    r, g, b, w = (int(i) for i in input().split())
    res = "NO"
    o = sum(x & 1 for x in (r, g, b, w))
    if o <= 1:
        res = "YES"
    else:
        m = min(r, g, b)
        if m > 0 and sum(x & 1 for x in (r - 1, g - 1, b - 1, w + 3)) <= 1:
            res = "YES"
        elif sum(x & 1 for x in (r - m, g - m, b - m, w + 3 * m)) <= 1:
            res = "YES"
    print(res)
