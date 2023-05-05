n, m = (int(i) for i in input().split())
p = [[c for c in input()] for _ in range(n)]
res, face = 0, set(list("face"))
for r in range(1, n):
    for c in range(1, m):
        res += set([p[r - 1][c - 1], p[r - 1][c], p[r][c - 1], p[r][c]]) == face
print(res)
