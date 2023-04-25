from collections import deque

n = int(input())
par = {}
for i in range(n):
    p = int(input())
    pa = par.get(p, [])
    par[p] = pa
    pa.append(i + 1)
res, q = 0, deque(par[-1])
while q:
    for _ in range(len(q)):
        sup = q.popleft()
        sub = par.get(sup, [])
        for e in sub:
            q.append(e)
    res += 1
print(res)
