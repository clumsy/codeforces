from math import inf


t = int(input())
for _ in range(t):
    n = int(input())
    a = (int(i) for i in input().split())
    sa = sb = 0
    ma = mb = inf
    for i in a:
        sa += i
        ma = min(ma, i)
    b = (int(i) for i in input().split())
    for i in b:
        sb += i
        mb = min(mb, i)
    res = min(sa + n * mb, sb + n * ma)
    print(res)
