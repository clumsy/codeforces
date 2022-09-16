n, m = (int(i) for i in input().split())
s = [[c for c in input()] for _ in range(n)]
min_r, max_r, min_c, max_c = n, -1, m, -1
for r in range(n):
    for c in range(m):
        if s[r][c] == "*":
            min_r, max_r = min(min_r, r), max(max_r, r)
            min_c, max_c = min(min_c, c), max(max_c, c)
res = "\n".join("".join(r[min_c : max_c + 1]) for r in s[min_r : max_r + 1])
print(res)
