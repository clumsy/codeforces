n, m = (int(i) for i in input().split())
a = [[i for i in input()] for _ in range(n)]
x, y = 0, 0
for r in range(n):
    for c in range(m):
        if a[r][c] == "*":
            x ^= r
            y ^= c
res = (i + 1 for i in (x, y))
print(*res)
