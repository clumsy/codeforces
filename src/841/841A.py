from collections import Counter

n, k = (int(i) for i in input().split())
cnt = Counter(input())
res = "YES" if all(v <= k for v in cnt.values()) else "NO"
print(res)
