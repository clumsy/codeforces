from functools import reduce
from operator import or_, and_

t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res = reduce(or_, a) - reduce(and_, a)
    print(res)
