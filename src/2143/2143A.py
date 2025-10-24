t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    if n < 3:
        res = "YES"
    else:
        p2, p1 = next(a), next(a)
        res = 1 if p2 > p1 else 0
        for e in a:
            res += p1 > max(e, p2)
            p1, p2 = e, p1
        res += p1 > p2
        res = "YES" if res == 1 else "NO"
    print(res)
