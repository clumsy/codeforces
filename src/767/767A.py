from heapq import heappush, heappop

n, a = int(input()), (int(i) for i in input().split())
q = []
for i in a:
    heappush(q, -i)
    res = []
    while q and n == -q[0]:
        res.append(-heappop(q))
        n -= 1
    print(*res)
