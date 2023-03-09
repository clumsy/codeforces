n, t = int(input()), [int(i) for i in input().split()]
res = prev = cur = 0
for i in range(n):
    if i > 0 and t[i] != t[i - 1]:
        res = max(res, 2 * min(prev, cur))
        prev, cur = cur, 1
    else:
        cur += 1
res = max(res, 2 * min(prev, cur))
print(res)
