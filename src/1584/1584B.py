t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    if n == 1 and m == 1:
        res = 0
    else:
        if n > m:
            n, m = m, n
        md, mr = divmod(m, 3)
        res = md * n
        if mr == 1:
            nd, nr = divmod(n, 3)
            # merge with 3 on the right, split in half to create 2x 2 if 1, for two it's just 1 extra
            res += nd + (nr > 0)
        elif mr == 2:
            nd, nr = divmod(n, 3)
            res += 2 * nd + nr
        print(res)
