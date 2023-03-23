from collections import Counter

t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    c = Counter(a)
    res = c.get(1, 0) * (2 ** c.get(0, 0))
    print(res)
