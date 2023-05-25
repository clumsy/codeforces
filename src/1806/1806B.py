from collections import Counter

t = int(input())
for _ in range(t):
    n, a = int(input()), Counter(int(i) for i in input().split())
    res = 0 if a[0] <= (n + 1) // 2 else 1 if n == a[0] or a[0] + a[1] != n else 2
    print(res)
