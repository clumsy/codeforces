from collections import Counter


t = int(input())
for _ in range(t):
    n = int(input())
    a = (int(i) for i in input().split())
    cnt = Counter(a)
    o = sum(v == 1 for v in cnt.values())
    res = 2 * ((o + 1) // 2) + len(cnt) - o
    print(res)
