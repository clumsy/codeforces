from collections import Counter

n, s = int(input()), input()
cnt = Counter(s)
res = 0 if cnt["I"] > 1 else 1 if cnt["I"] == 1 else cnt["A"] if cnt["A"] else 0
print(res)
