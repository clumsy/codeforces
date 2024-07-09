from heapq import heappush, heappop, heapify
from functools import reduce
from operator import mul


t = int(input())
for _ in range(t):
    a, b, c = (int(i) for i in input().split())
    m = [a, b, c]
    heapify(m)
    for _ in range(5):
        i = heappop(m)
        heappush(m, i + 1)
    res = reduce(mul, m, 1)
    print(res)
