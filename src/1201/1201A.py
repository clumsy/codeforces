from collections import Counter

n, m = (int(i) for i in input().split())
ma = [0] * m
cnt = [Counter() for _ in range(m)]
for _ in range(n):
    for i, c in enumerate(input()):
        new_cnt = cnt[i].get(c, 0) + 1
        cnt[i][c] = new_cnt
        ma[i] = max(ma[i], new_cnt)
a = (int(i) for i in input().split())
res = sum(i * c for i, c in zip(a, ma))
print(res)
