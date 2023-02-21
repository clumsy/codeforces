t = int(input())
for _ in range(t):
    n = int(input())
    lo, hi = 0, n - 1
    res = []
    while lo <= hi:
        res.append((3 * lo + 2, 3 * hi + 3))
        lo += 1
        hi -= 1
    print(len(res))
    for pair in res:
        print(*pair)
