t = int(input())
for _ in range(t):
    _, s = input(), input()
    res, i, c = 0, 0, 0
    while i < len(s):
        d = s[i]
        while i < len(s) and s[i] == d:
            c += 1
            i += 1
        c = c & 1
        res += 1 if c else 0
    print(res)
