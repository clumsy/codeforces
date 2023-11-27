g = [[int(i) for i in input().split()] for _ in range(3)]
# x + a + b = K
# c + y + d = K
# e + f + z = K
# x + z = e + b
# x + z + a + b + e + f = 2K
# (e + b) + a + b + e + f = 2K
# 2(e + b) + a + f = 2K
K = (2 * (g[2][0] + g[0][2]) + g[0][1] + g[2][1]) // 2
g[0][0] = K - (g[0][1] + g[0][2])
g[1][1] = K - (g[1][0] + g[1][2])
g[2][2] = K - (g[2][0] + g[2][1])
res = g
for r in res:
    print(*r)
