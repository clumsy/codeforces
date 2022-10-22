n, s = int(input()), input()
res = 0
for i in range(1, n):
    res += s[i] == s[i - 1]
print(res)
