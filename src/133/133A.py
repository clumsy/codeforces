from collections import Counter

s = input()
cnt = Counter(s)
res = "YES" if cnt["H"] + cnt["Q"] + cnt["9"] > 0 else "NO"
print(res)
