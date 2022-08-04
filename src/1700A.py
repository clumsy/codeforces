t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    # optimal path is always along the first row and last column
    res = m * (m - 1) // 2 + (m + m * n) * n // 2
    print(res)
