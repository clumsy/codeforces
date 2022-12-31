n, a = int(input()), [int(i) for i in input().split()]
cnt, sum, res = {}, 0, [1] * n
for i in a:
    cnt[i] = cnt.get(i, 0) + 1
for i in reversed(sorted(cnt.keys())):
    cnt[i], sum = sum, sum + cnt[i]
for i in range(n):
    res[i] += cnt[a[i]]
print(*res)
