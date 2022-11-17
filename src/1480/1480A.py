t = int(input())
for _ in range(t):
    s = input()
    res = []
    for i, c in enumerate(s):
        if i & 1 == 0:
            res.append("b" if c == "a" else "a")
        else:
            res.append("y" if c == "z" else "z")
    res = "".join(res)
    print(res)
