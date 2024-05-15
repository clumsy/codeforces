t = int(input())
for _ in range(t):
    a, b, c, d = (int(i) for i in input().split())
    if min(a, b) > min(c, d):
        a, b, c, d = c, d, a, b
    res = (
        "YES"
        if min(a, b) < min(c, d) and max(c, d) > max(a, b) and max(a, b) > min(c, d)
        else "NO"
    )
    print(res)
