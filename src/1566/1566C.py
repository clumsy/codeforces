t = int(input())
for k in range(t):
    n = int(input())
    f, s = (input() for _ in range(2))
    res = i = 0
    had_ones = False
    while i < n:
        if f[i] != s[i]:
            res += 2
            i += 1
            had_ones = False
        elif f[i] == s[i] == "0":
            if had_ones:
                res += 1
            elif i < n - 1 and f[i + 1] == s[i + 1] == "1":
                res += 1
                i += 1
            res += 1
            i += 1
            had_ones = False
        else:
            i += 1
            had_ones = True
    print(res)
