t = int(input())
for _ in range(t):
    n, a, b = (int(i) for i in input().split())
    lft = {a, *range(b + 1, n + 1)}
    rgt = {b, *range(1, a)}
    if max(len(lft), len(rgt)) > n // 2:
        res = [-1]
    else:
        for i in range(1, n + 1):
            if i in lft or i in rgt:
                continue
            if len(lft) < n // 2:
                lft.add(i)
            else:
                rgt.add(i)
        res = list(lft) + list(rgt)
    print(*res)
