s, t = (input() for _ in range(2))


def pos_to_xy(p):
    return ord(p[0]) - ord("a"), 8 - int(p[1])


sx, sy = pos_to_xy(s)
tx, ty = pos_to_xy(t)
dx, dy = tx - sx, ty - sy
res = []
while dx != 0 or dy != 0:
    if dx != 0 and dy != 0:
        if dx > 0 and dy > 0:
            res.append("RD")
            dx -= 1
            dy -= 1
        if dx < 0 and dy < 0:
            res.append("LU")
            dx += 1
            dy += 1
        if dx > 0 and dy < 0:
            res.append("RU")
            dx -= 1
            dy += 1
        if dx < 0 and dy > 0:
            res.append("LD")
            dx += 1
            dy -= 1
    elif dy != 0:
        res.append("D" if dy > 0 else "U")
        dy += -1 if dy > 0 else 1
    elif dx != 0:
        res.append("R" if dx > 0 else "L")
        dx += -1 if dx > 0 else 1
print(len(res))
print(*res, sep="\n")
