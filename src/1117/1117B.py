from heapq import heappop, heappush

n, m, k = (int(i) for i in input().split())
a = (int(i) for i in input().split())
e = []
for i in a:
    heappush(e, i)
    if len(e) > 2:
        heappop(e)
d, r = divmod(m, k + 1)
res = d * (e[1] * k + e[0] * 1) + e[1] * r
print(res)
