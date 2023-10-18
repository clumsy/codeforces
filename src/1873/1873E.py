from math import inf

t = int(input())
for _ in range(t):
    n, x = (int(i) for i in input().split())
    a = sorted(int(i) for i in input().split()) + [inf]
    res = a[0]
    for i, e in enumerate(a):
        if i == 0 or e == a[i - 1]:
            continue
        dh = min(e - a[i - 1], x // i)
        if dh == 0:
            break
        res += dh
        x -= dh * i
    print(res)
