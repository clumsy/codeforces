t = int(input())
for _ in range(t):
    a, b, L = (int(i) for i in input().split())
    q = [(1, 1)]
    res = set()
    while q:
        a1, b1 = q.pop()
        res.add(L // (a1 * b1))
        for a_, b_ in [(a, 1), (1, b)]:
            d, r = divmod(L, a1 * a_ * b1 * b_)
            if d not in res and d > 0 and r == 0:
                q.append((a1 * a_, b1 * b_))
    res = len(res)
    print(res)
