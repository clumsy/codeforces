from heapq import heappop, heappush

n, a = int(input()), (int(i) for i in input().split())
mins, maxs = [], []
for i in a:
    heappush(mins, -i)
    if len(mins) > 2:
        heappop(mins)
    heappush(maxs, i)
    if len(maxs) > 2:
        heappop(maxs)
res = min(maxs[0] + mins[1], maxs[1] + mins[0])
print(res)
