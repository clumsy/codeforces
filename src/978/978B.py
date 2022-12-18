n, s = int(input()), input()
res = 0
for i, c in enumerate(s):
    if i > 1 and s[i] == s[i - 1] == s[i - 2] == "x":
        res += 1
print(res)
