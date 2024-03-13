from collections import Counter


t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    cnt = Counter(a).values()
    res = "YES" if len(cnt) < 3 and max(cnt) - min(cnt) < 2 else "NO"
    print(res)
