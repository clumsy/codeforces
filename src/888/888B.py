from collections import Counter

n, a = int(input()), Counter(input())
res = 2 * (min(a["L"], a["R"]) + min(a["U"], a["D"]))
print(res)
