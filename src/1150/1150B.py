n = int(input())
grid = [[c for c in input()] for _ in range(n)]
for r in range(1, n - 1):
    for c in range(1, n - 1):
        if (
            grid[r][c]
            == grid[r - 1][c]
            == grid[r + 1][c]
            == grid[r][c - 1]
            == grid[r][c + 1]
            == "."
        ):
            grid[r][c] = grid[r - 1][c] = grid[r + 1][c] = grid[r][c - 1] = grid[r][
                c + 1
            ] = "#"
res = "YES" if all(grid[r][c] == "#" for r in range(n) for c in range(n)) else "NO"
print(res)
