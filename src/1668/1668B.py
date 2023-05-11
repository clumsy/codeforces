from math import inf

t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    res, ma, mi = 0, 0, inf
    for i in a:
        ma, mi = max(ma, i), min(mi, i)
        res += i + 1  # need chairs to right, when sorted (including self)
    res = "YES" if m >= res + ma - mi else "NO"
    print(res)
