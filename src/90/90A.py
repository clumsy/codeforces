r, g, b = (int(i) for i in input().split())
res = 3 * ((r + 1) // 2 - 1)
if g:
    res = max(res, 1 + 3 * ((g + 1) // 2 - 1))
if b:
    res = max(res, 2 + 3 * ((b + 1) // 2 - 1))
res += 30
print(res)
