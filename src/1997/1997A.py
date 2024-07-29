t = int(input())
for _ in range(t):
    s = input()
    for i, c in enumerate(s):
        if i and c == s[i - 1]:
            res = s[:i] + ("a" if s[i] != "a" else "b") + s[i:]
            break
    else:
        res = ("a" if s[0] != "a" else "b") + s
    print(res)
