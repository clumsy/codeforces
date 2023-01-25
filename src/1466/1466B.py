t = int(input())
for _ in range(t):
    n, x = int(input()), sorted(int(i) for i in input().split())
    res, cur = 0, 0
    for i in range(n):
        if x[i] >= cur:
            res += 1
            cur = max(x[i], cur + 1)
    print(res)
