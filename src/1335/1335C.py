from collections import Counter


t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    cnt = Counter(a)
    ma = max(cnt.values())
    res = max(min(ma, len(cnt) - 1), min(ma - 1, len(cnt)))
    print(res)
