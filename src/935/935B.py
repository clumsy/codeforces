n, s = int(input()), input()
res, x, y = 0, 0, 0
d = {
    "U": (0, +1),
    "D": (0, -1),
    "R": (+1, 0),
    "L": (-1, 0),
}
cur = None
for c in s:
    prev = cur
    x, y = (i + di for i, di in zip((x, y), d[c]))
    cur = prev if y == x else y > x
    if prev is not None and prev != cur:
        res += 1
print(res)
