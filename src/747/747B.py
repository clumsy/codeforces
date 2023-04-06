from collections import Counter

n, s = int(input()), input()
res = [c for c in s]
cnt = Counter(c for c in s if c != "?")
if n % 4 != 0 or max(cnt.values(), default=0) * 4 > n:
    res = "==="
else:
    for i, c in enumerate(s):
        if c == "?":
            for g in ["A", "C", "G", "T"]:
                if cnt[g] < n // 4:
                    res[i] = g
                    cnt[g] += 1
                    break
    res = "".join(res)
print(res)
