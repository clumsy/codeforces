t = int(input())
for _ in range(t):
    s = input()
    if s[0] != s[-1]:
        a = s.rfind("a", 1, len(s) - 1)
        if a >= 0:
            res = s[:a], s[a], s[a + 1 :]
        else:
            res = s[0], s[1:-1], s[-1]
    else:
        res = s[0], s[1:-1], s[-1]
    print(*res)
