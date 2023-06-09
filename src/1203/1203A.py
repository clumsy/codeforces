from collections import Counter

t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    diffs = Counter()
    for i in range(n):
        diffs[a[i] - a[i - 1]] += 1
    res = (
        "YES"
        if diffs == Counter({0: 1})
        or diffs == Counter({1: n - 1, -n + 1: 1})
        or diffs == Counter({-1: n - 1, n - 1: 1})
        else "NO"
    )
    print(res)
