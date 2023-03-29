from collections import Counter

n, s = int(input()), input()
cnt, res = Counter(), s[:2]
for i in range(n - 1):
    cur = s[i : i + 2]
    cnt[cur] += 1
    if cnt[cur] > cnt[res]:
        res = cur
print(res)
