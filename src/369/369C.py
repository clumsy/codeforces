from collections import defaultdict


n = int(input())
g = defaultdict(list)
bad = set()
for _ in range(n - 1):
    x, y, t = (int(i) for i in input().split())
    g[x].append(y)
    g[y].append(x)
    if t == 2:
        bad.add(x)
        bad.add(y)

res, vis, stk, cnt = [], set(), [(1, -1)], defaultdict(int)
while stk:
    cur, prt = stk[-1]
    if cur in vis:
        stk.pop()
        cnt[prt] += cnt[cur] + (cur in bad)
        if cnt[cur] == 1:
            res.append(cur)
    else:
        vis.add(cur)
        cnt[cur] = int(cur in bad)
        for nxt in g[cur]:
            if nxt != prt:
                stk.append((nxt, cur))

print(len(res))
print(*res)
