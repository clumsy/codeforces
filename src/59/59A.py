s = input()
res = s.lower() if 2 * sum(1 for c in s if c.islower()) >= len(s) else s.upper()
print(res)
