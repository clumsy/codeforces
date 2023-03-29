from collections import Counter

s = Counter(input())
res = "YES" if s["-"] == 0 or s["o"] == 0 or s["-"] % s["o"] == 0 else "NO"
print(res)
