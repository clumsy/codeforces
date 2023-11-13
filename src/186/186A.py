from collections import Counter

f, s = (input() for _ in range(2))
res = "NO"
if len(f) == len(s):
    cnt, prv = Counter(), []
    for i in range(len(f)):
        cnt[f[i]] += 1
        if f[i] != s[i]:
            if not prv or (len(prv) == 1 and f[prv[0]] == s[i] and f[i] == s[prv[0]]):
                prv.append(i)
                res = "YES" if len(prv) == 2 else "NO"
                continue
            res = "NO"
            break
    if not prv and len(cnt) < len(f):
        res = "YES"
print(res)
