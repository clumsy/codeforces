from math import ceil

n = int(input())
s, d = [0] * n, [0] * n
for i in range(n):
    s[i], d[i] = (int(k) for k in input().split())
res = s[0]
for i in range(1, n):
    k = max(ceil((res + 1 - s[i]) / d[i]), 0)
    res = s[i] + k * d[i]
print(res)
