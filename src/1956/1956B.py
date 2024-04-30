from collections import Counter


t = int(input())
for _ in range(t):
    n = int(input())
    a = (int(i) for i in input().split())
    cnt = Counter(a)
    res = sum(v == 2 for v in cnt.values())
    print(res)
