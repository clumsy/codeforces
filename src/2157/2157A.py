from collections import Counter


t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    cnt = Counter(a)
    res = sum(v if v < k else v - k for k, v in cnt.items())
    print(res)
