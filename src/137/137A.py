s = input()
res, cur = 0, 1
for i in range(1, len(s)):
    if s[i] != s[i - 1] or cur == 5:
        res += 1
        cur = 0
    cur += 1
res += cur > 0
print(res)
