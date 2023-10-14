t = int(input())
for _ in range(t):
    n = int(input())
    res, seen, left = [], set(), range(1, n + 1)
    for i in range(1, n + 1):
        if i not in seen:
            while i <= n and i not in seen:
                seen.add(i)
                res.append(i)
                i *= 2
    print(*res)
