from collections import Counter

t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = max(Counter(a).values())
    print(res)
