import heapq

t = int(input())
for _ in range(t):
    _, a = input(), (int(i) for i in input().split())
    h = []
    for i in a:
        heapq.heappush(h, i)
        if len(h) > 2:
            heapq.heappop(h)
    res = sum(h)
    print(res)
