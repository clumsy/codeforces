from heapq import heappush, heappop

t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res, h = 0, []
    for i in a:
        if i == 0:
            res += -heappop(h) if h else 0
        else:
            heappush(h, -i)
    print(res)
