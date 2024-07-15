from collections import Counter


t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    cnt = Counter(a)
    # m = mc = 0
    # for i in a:
    #     if i > m:
    #         m, mc = i, 0
    #     mc += i == m
    # res = "YES" if mc & 1 == 1 else "NO"
    res = "YES" if any(v & 1 == 1 for v in cnt.values()) else "NO"
    print(res)
