from math import gcd

t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    mi, res = min(a), -1
    for i in a:
        if i != mi:
            res = i - mi if res < 0 else gcd(res, i - mi)
        if res == 1:
            break
    print(res)
