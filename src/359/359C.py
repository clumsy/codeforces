from collections import defaultdict


n, x = (int(i) for i in input().split())
a = [int(i) for i in input().split()]
# (x^(s - a1) + ... + x^(s - an)) / x^s
# x^(s - an) * (1 + x^(an - an-1) + ... + x^(an - a1))
cnt = defaultdict(int)
s = sum(a)
for i in a:
    cnt[s - i] += 1
p = s - a[-1]
while cnt[p] % x == 0:
    cnt[p + 1] += cnt[p] // x
    p += 1
p = min(p, s)
mod = 10**9 + 7
res = 1
b = x
while p > 0:
    p, r = divmod(p, 2)
    if r == 1:
        res = (res * b) % mod
    b = (b * b) % mod
print(res)
