from collections import Counter

t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    cnt = Counter(a)
    res = "YES" if n > 1 and 2 * cnt[1] + (n - cnt[1]) <= sum(a) else "NO"
    print(res)
