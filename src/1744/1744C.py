t = int(input())
for _ in range(t):
    n, c = input().split()
    s = input()
    n, s = int(n), s + s
    res, p = 0, None
    for i in range(len(s)):
        if s[i] == c and p is None:
            p = i
        if s[i] == "g":
            res, p = max(res, i - (p or i)), None
    print(res)
