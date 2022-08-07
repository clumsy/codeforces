t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    a = [[int(i) for i in input().split()] for j in range(n)]
    max_r, max_c = 0, 0
    for r in range(n):
        for c in range(m):
            if a[r][c] > a[max_r][max_c]:
                max_r, max_c = r, c
    h, w = max(max_r + 1, n - max_r), max(max_c + 1, m - max_c)
    print(h * w)
