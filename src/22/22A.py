from heapq import heappush, heappop


n, a = int(input()), (int(i) for i in input().split())
h = []
for i in a:
    if -i not in h:
        heappush(h, -i)
        if len(h) > 2:
            heappop(h)
res = -h[0] if len(h) > 1 else "NO"
print(res)
