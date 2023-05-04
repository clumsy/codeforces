n = 3
p = [[int(i) for i in input().split()] for _ in range(n)]
for r in range(n):
    for c in range(n):
        cnt = (
            p[r][c]
            + (p[r - 1][c] if r > 0 else 0)
            + (p[r + 1][c] if r < n - 1 else 0)
            + (p[r][c - 1] if c > 0 else 0)
            + (p[r][c + 1] if c < n - 1 else 0)
        )
        print(1 - cnt & 1, end="")
    print()
