s, t = input(), input()
res, i = 1, 0
while res <= len(s) and i < len(t):
    if s[res - 1] == t[i]:
        res += 1
    i += 1
print(res)
