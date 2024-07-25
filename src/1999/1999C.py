t = int(input())
for _ in range(t):
    n, s, m = (int(i) for i in input().split())
    r0, res = 0, "NO"
    for _ in range(n):
        l, r = (int(i) for i in input().split())
        if l - r0 >= s:
            res = "YES"
        r0 = r
    res = "YES" if m - r0 >= s else res
    print(res)
