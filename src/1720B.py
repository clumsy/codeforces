import heapq

t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    maxs, mins = [], []
    for i in a:
        heapq.heappush(maxs, +i)
        if len(maxs) > 2:
            heapq.heappop(maxs)
        heapq.heappush(mins, -i)
        if len(mins) > 2:
            heapq.heappop(mins)
    # we can always pick l and r such that it separates two maximums and two minimums
    print(sum(maxs) + sum(mins))
