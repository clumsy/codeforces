from collections import Counter

s = Counter(input())
res = min(s["B"], s["u"] // 2, s["l"], s["b"], s["a"] // 2, s["r"], s["s"])
print(res)
