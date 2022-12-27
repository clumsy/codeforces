n, s = int(input()), input()
res, vowels = [""] * n, "aeiuoy"
for i, c in enumerate(s):
    res[i] = "" if i > 0 and c in vowels and s[i - 1] in vowels else c
res = "".join(res)
print(res)
