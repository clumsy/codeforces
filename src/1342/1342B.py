t = int(input())
for _ in range(t):
    s = input()
    if s.count(s[0]) == len(s):
        res = s
    else:
        res = []
        for c in s:
            if res and c == res[-1]:
                res.append("0" if c == "1" else "1")
            res.append(c)
        res = "".join(res)
    print(res)
