from collections import Counter

s = Counter(input())
res = 4 if s["4"] >= s["7"] and s["4"] > 0 else 7 if s["7"] > 0 else -1
print(res)
