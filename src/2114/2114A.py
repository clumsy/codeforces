from math import isqrt


t = int(input())
for _ in range(t):
    s = input()
    s = int(s.lstrip("0") or "0")
    r = isqrt(s)
    res = [-1] if r * r != s else [0, r]
    print(*res)
