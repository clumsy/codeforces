t = int(input())
for _ in range(t):
    s = input()
    res, n = 0, len(s)
    for i in range(1, n):
        res += s[i] == s[i - 1] == "_"
    res += s.startswith("_")
    res += s.endswith("_")
    res += s == "^"
    print(res)
