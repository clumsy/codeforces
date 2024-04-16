from collections import Counter

t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    cnt = Counter(s)
    res = sum(ord(c) - ord("A") + 1 <= k for c, k in cnt.items())
    print(res)
