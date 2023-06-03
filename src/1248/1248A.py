from collections import Counter

t = int(input())
for _ in range(t):
    n, p = int(input()), (int(i) for i in input().split())
    m, q = int(input()), (int(i) for i in input().split())
    p = Counter(i & 1 for i in p)
    q = Counter(i & 1 for i in q)
    res = p[0] * q[0] + p[1] * q[1]
    print(res)
