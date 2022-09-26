q = input()
res = "YES" if next(c for c in reversed(q) if c.isalpha()).lower() in "aeiouy" else "NO"
print(res)
