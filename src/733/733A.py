s = input().lower()
vowels = "aoueiy"
res, prev = 1, -1
for i, c in enumerate(s):
    if c in vowels:
        res = max(res, i - prev)
        prev = i
res = max(res, i + 1 - prev)
print(res)
