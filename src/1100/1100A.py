from collections import Counter

n, k = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
cnt = Counter(a)
res = 0
for i in range(k):
    rem = Counter(a[j] for j in range(i, n, k))
    diff = cnt - rem
    res = max(res, abs(diff[1] - diff[-1]))
print(res)
