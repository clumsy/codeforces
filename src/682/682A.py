from collections import Counter

n, m = (int(i) for i in input().split())
x_cnt = Counter(i % 5 for i in range(1, n + 1))
y_cnt = Counter(i % 5 for i in range(1, m + 1))
res = sum(x_cnt[i] * y_cnt[(5 - i) % 5] for i in range(5))
print(res)
