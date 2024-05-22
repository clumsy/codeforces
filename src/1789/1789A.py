from math import gcd
from collections import Counter

t = int(input())
for _ in range(t):
    n, a = int(input()), Counter(int(i) for i in input().split())

    res = "YES" if a[1] > 0 or a[2] > 1 else "NO"
    a = list(a.keys())
    k = len(a)
    for i in range(k):
        if res == "YES":
            break
        for j in range(i + 1, k):
            if gcd(a[i], a[j]) < 3:
                res = "YES"
                break
    print(res)
