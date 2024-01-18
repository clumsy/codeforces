from heapq import heappush, heappop


n, s = (int(i) for i in input().split())
q = []
for _ in range(n):
    hh, mm = (int(i) for i in input().split())
    heappush(q, hh * 60 + mm)
prv, res = -s - 1, None
while q:
    nxt = heappop(q)
    if nxt - prv - 1 >= 2 * s + 1:
        res = prv + s + 1
        break
    prv = nxt
res = res or (prv + s + 1)
res = divmod(res, 60)
print(*res)
