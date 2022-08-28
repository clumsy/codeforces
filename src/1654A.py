from heapq import heappush, heappop

t = int(input())
for _ in range(t):
    _, a = input(), (int(i) for i in input().split())
    h = []
    for i in a:
        heappush(h, i)
        if len(h) > 2:
            heappop(h)
    res = sum(h)
    print(res)
