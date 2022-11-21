s = sorted(int(i) for i in input().split())
res = 0
for i in range(1, len(s)):
    res += s[i] == s[i - 1]
print(res)
