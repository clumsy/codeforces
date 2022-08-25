from functools import reduce
from operator import ior

t = int(input())
for _ in range(t):
    _, a = input(), (int(i) for i in input().split())
    res = reduce(ior, a)
    print(res)
