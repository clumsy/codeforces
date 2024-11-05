t = int(input())
for _ in range(t):
    n, m, r, c = (int(i) for i in input().split())
    res = m - c + (n - r) * (2 * m - 1)
    print(res)
