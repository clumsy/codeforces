t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    lft = mid = rgt = 0
    res = "YES"
    for i, e in enumerate(a):
        lft, mid = mid, rgt
        if e - lft < 0:
            res = "NO"
        elif i < n - 2:
            rgt = e - lft
            mid += 2 * rgt
        elif e != lft:
            res = "NO"
    print(res)
