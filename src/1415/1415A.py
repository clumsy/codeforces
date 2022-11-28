t = int(input())
for _ in range(t):
    n, m, r, c = (int(i) for i in input().split())
    res = max(r - 1, n - r) + max(c - 1, m - c)
    print(res)
