t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    # [m] -> 0
    # [0, m] -> m
    # [0, m, 0] -> 2 * m
    res = min(2, n - 1) * m
    print(res)
