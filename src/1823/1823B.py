t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    p = [int(i) for i in input().split()]
    exch = []
    for i in range(n):
        if abs(i + 1 - p[i]) % k != 0:
            exch.append(i)
    res = (
        0
        if not exch
        else 1
        if len(exch) == 2
        and abs(exch[0] + 1 - p[exch[1]]) % k == abs(exch[1] + 1 - p[exch[0]]) % k == 0
        else -1
    )
    print(res)
