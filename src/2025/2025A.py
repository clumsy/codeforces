t = int(input())
for _ in range(t):
    s, t = (input() for _ in range(2))
    c = 0
    for i in range(min(len(s), len(t))):
        if s[i] != t[i]:
            break
        c += 1
    res = min(c + 1 + len(s) - c + len(t) - c, len(s) + len(t))
    print(res)
