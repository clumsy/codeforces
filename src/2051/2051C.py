t = int(input())
for _ in range(t):
    n, m, k = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    q = (int(i) for i in input().split())
    mis = sum(range(1, n + 1)) - sum(q)
    res = []
    for i in a:
        if k == n:
            res.append("1")
        elif k < n - 1:
            res.append("0")
        else:
            res.append("1" if i == mis else "0")
    res = "".join(res)
    print(res)
