from collections import Counter

n, s = int(input()), input()
res = "YES" if n >= 26 and len(Counter(c.lower() for c in s).keys()) == 26 else "NO"
print(res)
