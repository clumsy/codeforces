n = int(input())
s = input()
p = input()
res = 0
for i in range(n):
    d = abs(ord(s[i]) - ord(p[i]))
    res += min(d, 10 - d)
print(res)
