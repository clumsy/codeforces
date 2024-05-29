g = [input() for _ in range(3)]
res = "CCC"
for r1 in range(3):
    for c1 in range(3):
        for dr2 in (-1, 0, 1):
            for dc2 in (-1, 0, 1):
                r2, c2 = r1 + dr2, c1 + dc2
                if 0 <= r2 < 3 and 0 <= c2 < 3 and len(set([(r1, c1), (r2, c2)])) == 2:
                    for dr3 in (-1, 0, 1):
                        for dc3 in (-1, 0, 1):
                            r3, c3 = r2 + dr3, c2 + dc3
                            if (
                                0 <= r3 < 3
                                and 0 <= c3 < 3
                                and len(set([(r1, c1), (r2, c2), (r3, c3)])) == 3
                            ):
                                res = min(res, g[r1][c1] + g[r2][c2] + g[r3][c3])
print(res)
