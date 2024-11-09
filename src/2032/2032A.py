from collections import Counter


t = int(input())
for _ in range(t):
    n, a = int(input()), Counter(input().split())
    mi, ma = a["1"] & 1, 2 * n - a["1"] if a["1"] > n else a["1"]
    res = mi, ma
    print(*res)
