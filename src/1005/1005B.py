s, t = input()[::-1], input()[::-1]
n, m, i = len(s), len(t), 0
while i < min(n, m):
    if s[i] != t[i]:
        break
    i += 1
res = m - i + n - i
print(res)
