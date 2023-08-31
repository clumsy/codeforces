from heapq import heappush, heappop

t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    h = []
    for i in range(1, n):
        heappush(h, abs(a[i] - a[i - 1]))
        if len(h) > k - 1:
            heappop(h)
    res = -sum(h)
    for i in range(1, n):
        res += abs(a[i] - a[i - 1])
    print(res)
