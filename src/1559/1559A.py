from functools import reduce
from operator import iand

t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = reduce(iand, a)
    print(res)
