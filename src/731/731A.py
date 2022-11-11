s = input()
res = 0
for i, e in enumerate(s):
    diff = abs(ord(s[i]) - ord(s[i - 1] if i > 0 else "a"))
    res += min(diff, 26 - diff)
print(res)
