t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    mi = s.rfind(min(s))
    res = s[mi] + s[:mi] + s[mi + 1 :]
    print(res)
