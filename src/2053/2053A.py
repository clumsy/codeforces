t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = "NO"
    p = next(a)
    for i in a:
        if 2 * min(p, i) > max(p, i):
            res = "YES"
            break
        p = i
    print(res)
