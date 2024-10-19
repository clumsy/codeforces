from math import gcd


t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    a = [i for i in a if i & 1 == 0] + [i for i in a if i & 1 == 1]
    res = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            res += a[i] & 1 == 0 or gcd(a[i], 2 * a[j]) > 1
    print(res)
