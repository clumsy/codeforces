from heapq import heapify, heappush, heappop

t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    heapify(a)
    b = (int(i) for i in input().split())
    for i in b:
        heappop(a)
        heappush(a, i)
    res = sum(a)
    print(res)
