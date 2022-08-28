from heapq import heappush, heappop

t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    maxs, mins = [], []
    for i in a:
        heappush(maxs, +i)
        if len(maxs) > 2:
            heappop(maxs)
        heappush(mins, -i)
        if len(mins) > 2:
            heappop(mins)
    # we can always pick l and r such that it separates two maximums and two minimums
    print(sum(maxs) + sum(mins))
