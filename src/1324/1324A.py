from collections import Counter

t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = "YES" if len(Counter(i & 1 for i in a)) == 1 else "NO"
    print(res)
