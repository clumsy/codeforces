t = int(input())
for _ in range(t):
    s, t = (input() for _ in range(2))
    res, t = [], list(t[::-1])
    for i in s:
        if (t and i == t[-1]) or i == "?":
            res.append(t.pop() if t else "a")
        else:
            res.append(i)
    if t:
        print("NO")
    else:
        print("YES")
        res = "".join(res)
        print(res)
