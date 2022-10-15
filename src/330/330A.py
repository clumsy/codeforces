r, c = (int(i) for i in input().split())
a = [[v for v in input()] for _ in range(r)]
rs = [any(a[i][j] == "S" for j in range(c)) for i in range(r)]
cs = [any(a[i][j] == "S" for i in range(r)) for j in range(c)]
res = 0
for i in range(r):
    for j in range(c):
        if not rs[i] or not cs[j]:
            res += 1
print(res)
