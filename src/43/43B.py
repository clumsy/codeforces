from collections import Counter

s1, s2 = (input() for _ in range(2))
cnt1, cnt2 = Counter(s1), Counter(s2)
del cnt2[" "]
res = "YES" if all(cnt2[c] <= cnt1[c] for c in cnt2) else "NO"
print(res)
