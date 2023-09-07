from math import inf
from heapq import heapify, heappop

t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    heapify(a)
    res, acc = -inf, 0
    while a:
        i = heappop(a)
        res = max(res, i - acc)
        acc += i - acc
    print(res)
