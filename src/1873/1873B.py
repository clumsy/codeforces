from math import prod

t = int(input())
for _ in range(t):
    n, a = int(input()), sorted(int(i) for i in input().split())
    a[0] += 1
    res = prod(a)
    print(res)
