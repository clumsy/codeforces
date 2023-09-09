from math import inf

t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    s = input()
    res, cur = inf, 0
    for i, c in enumerate(s):
        cur += 1 if c == "W" else 0
        if i >= k:
            cur -= 1 if s[i - k] == "W" else 0
        if i >= k - 1:
            res = min(res, cur)
    print(res)
