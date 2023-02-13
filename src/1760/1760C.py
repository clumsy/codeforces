from heapq import heappop, heappush

t = int(input())
for _ in range(t):
    n, s = int(input()), [int(i) for i in input().split()]
    m = []
    for e in s:
        heappush(m, e)
        if len(m) > 2:
            heappop(m)
    res = (e - m[1] if e < m[1] else e - m[0] for e in s)
    print(*res)
