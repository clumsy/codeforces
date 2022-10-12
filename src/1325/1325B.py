from collections import Counter

t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = len(Counter(a))
    print(res)
