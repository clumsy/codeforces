from math import inf

n, a = int(input()), (int(i) for i in input().split())
mi, s, cnt = inf, 0, 0
for i, e in enumerate(a):
    if e < mi:
        mi, i_mi = e, i + 1
    s += e
    cnt += 1
res = [] if cnt == 1 or 2 * mi == s else [i_mi]
if res:
    print(len(res))
    print(*res)
else:
    print(-1)
# s = sum(a)
# def dfs(g, c, i):
#     if i == n:
#         return g if 2 * c == s else None
#     g.append(i)
#     res = dfs(g, c + a[i], i + 1)
#     if res:
#         return res
#     g.pop()
#     return dfs(g, c, i + 1)

# res = dfs([], 0, 0)
# if res is None:
#     print(-1)
# else:
#     print(len(res))
#     print(*res)
