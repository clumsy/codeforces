from math import ceil

t = int(input())
for _ in range(t):
    n, x = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    mi, ma = 0, 0
    for i in a:
        ma += ceil(i / x)
        mi += i
    res = ceil(mi / x), ma
    print(*res)
