from collections import Counter

t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    s = Counter(input())
    res = [None] * k
    for i in range(k):
        for o in range(ord("z") - ord("a") + 1):
            c = chr(o + ord("a"))
            if o >= n // k or (s.get(c, 0) < k and (s.get(c, 0)) % k <= i):
                res[i] = c
                break
    res = "".join(res)
    print(res)
