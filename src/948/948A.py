rows, cols = (int(i) for i in input().split())
p = [list(input()) for _ in range(rows)]
res = "YES"
for r in range(rows):
    if res != "YES":
        break
    for c in range(cols):
        if p[r][c] == "W":
            if r > 0:
                if p[r - 1][c] == "S":
                    res = "NO"
                    break
                elif p[r - 1][c] == ".":
                    p[r - 1][c] = "D"
            if c > 0:
                if p[r][c - 1] == "S":
                    res = "NO"
                    break
                elif p[r][c - 1] == ".":
                    p[r][c - 1] = "D"
            if r < rows - 1:
                if p[r + 1][c] == "S":
                    res = "NO"
                    break
                elif p[r + 1][c] == ".":
                    p[r + 1][c] = "D"
            if c < cols - 1:
                if p[r][c + 1] == "S":
                    res = "NO"
                    break
                elif p[r][c + 1] == ".":
                    p[r][c + 1] = "D"
print(res)
if res == "YES":
    for r in range(rows):
        print("".join(p[r]))
