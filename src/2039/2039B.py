t = int(input())
for _ in range(t):
    s = input()
    res = "-1"
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            res = s[i - 1] + s[i]
            break
        elif i > 1 and s[i - 1] != s[i - 2] and s[i] != s[i - 2]:
            res = s[i - 2] + s[i - 1] + s[i]
            break
    print(res)
