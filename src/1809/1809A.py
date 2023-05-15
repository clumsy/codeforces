from collections import Counter

t = int(input())
for _ in range(t):
    s = sorted(v for v in Counter(input()).values())
    res = -1 if s[-1] == 4 else 6 if s[-1] == 3 else 4
    print(res)
