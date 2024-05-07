from collections import Counter


t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    s = input()
    cnt = Counter(s)
    vals = cnt.values()
    evens = sum(v - (v & 1) for v in vals)
    res = (
        "NO"
        if evens + (1 if (n - k) & 1 == 1 and any(v & 1 == 1 for v in vals) else 0)
        < n - k
        else "YES"
    )
    print(res)
