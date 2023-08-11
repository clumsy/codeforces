n = int(input())
a = (int(i) for i in input().split())
b = (int(i) for i in input().split())
pos = {v: i + 1 for i, v in enumerate(a)}
res, cur = [], 0
for i in b:
    p = pos[i]
    res.append(max(0, p - cur))
    cur = max(cur, p)
print(*res)
