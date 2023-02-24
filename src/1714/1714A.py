t = int(input())
for _ in range(t):
    n, H, M = (int(i) for i in input().split())
    before, after = None, None
    for _ in range(n):
        h, m = (int(i) for i in input().split())
        if (h, m) >= (H, M):
            after = min(after, (h, m)) if after else (h, m)
        else:
            before = min(before, (h, m)) if before else (h, m)
    if after:
        res = 60 * (after[0] - H) + (after[1] - M)
    else:
        res = 60 * (before[0] + 24 - H) + (before[1] - M)
    res = divmod(res, 60)
    print(*res)
