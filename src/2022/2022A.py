t = int(input())
for _ in range(t):
    n, r = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    res = lft = 0
    for i in a:
        d, x = divmod(i, 2)
        res += 2 * d
        lft += x
    r -= res // 2
    res += min(r, lft) - max(0, lft - r)
    print(res)
