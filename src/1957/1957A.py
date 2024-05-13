from collections import Counter


t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    cnt = Counter(a)
    res = sum(c // 3 for c in cnt.values())
    print(res)
