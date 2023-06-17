from collections import Counter

k, s = int(input()), Counter(input())
if any(v % k != 0 for v in s.values()):
    res = -1
else:
    res = []
    for c, v in s.items():
        res += c * (v // k)
    res *= k
    res = "".join(res)
print(res)
