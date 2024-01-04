from collections import defaultdict

n, m, k = (int(i) for i in input().split())
grid = defaultdict(lambda: defaultdict(bool))
res = 0
for j in range(k):
    r, c = (int(i) for i in input().split())
    grid[r][c] = True
    if (
        (grid[r][c - 1] and grid[r - 1][c - 1] and grid[r - 1][c])
        or (grid[r][c + 1] and grid[r - 1][c + 1] and grid[r - 1][c])
        or (grid[r][c - 1] and grid[r + 1][c - 1] and grid[r + 1][c])
        or (grid[r][c + 1] and grid[r + 1][c + 1] and grid[r + 1][c])
    ):
        res = j + 1
        break
print(res)
