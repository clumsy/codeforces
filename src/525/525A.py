from collections import Counter

n, s = int(input()) - 1, input()
res, cnt = 0, Counter()
for i in range(n):
    cnt[s[2 * i]] += 1
    c = s[2 * i + 1].lower()
    if cnt[c] == 0:
        res += 1
    else:
        cnt[c] -= 1
print(res)
