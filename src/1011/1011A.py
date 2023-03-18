n, k = (int(i) for i in input().split())
s = sorted(input())
res, n, prev = 0, len(s), None
for i, c in enumerate(s):
    if i > 0 and ord(c) - ord(prev) <= 1:
        continue
    res += ord(c) - ord("a") + 1
    prev = c
    k -= 1
    if k == 0:
        break
res = res if k == 0 else -1
print(res)
