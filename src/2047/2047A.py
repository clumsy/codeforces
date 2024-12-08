from math import isqrt


t = int(input())
for _ in range(t):
    n = int(input())
    a = (int(i) for i in input().split())
    res = s = 0
    for _ in range(n):
        s += next(a)
        if s & 1 == 1 and isqrt(s) ** 2 == s:
            res += 1
    print(res)
