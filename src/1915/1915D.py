C, V = "bcd", "ae"
t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    prv, res = 0, []
    for i in range(n):
        if i > 0 and s[i] in C and (s[i - 1] in C or (i + 1 < n and s[i + 1] in V)):
            res.append(s[prv:i])
            prv = i
    res.append(s[prv:])
    res = ".".join(res)
    print(res)
