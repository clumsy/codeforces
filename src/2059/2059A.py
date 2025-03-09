from collections import Counter


t = int(input())
for _ in range(t):
    n = int(input())
    a = (int(i) for i in input().split())
    b = (int(i) for i in input().split())
    ca, cb = Counter(a), Counter(b)
    res = "YES" if max(len(ca), len(cb)) >= 3 or len(ca) + len(cb) >= 4 else "NO"
    print(res)
