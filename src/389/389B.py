n = int(input())
g = [list(input()) for _ in range(n)]


def bad(r, c):
    if g[r][c] == ".":
        return False
    if r >= n - 2 or c == 0 or c == n - 1:
        return True
    check = [(r, c), (r + 1, c), (r + 2, c), (r + 1, c - 1), (r + 1, c + 1)]
    for x, y in check:
        if g[x][y] == ".":
            return True
        g[x][y] = "."
    return False


res = "YES"
for r in range(n):
    for c in range(n):
        if bad(r, c):
            res = "NO"
            break
print(res)
