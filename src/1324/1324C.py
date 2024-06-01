t = int(input())
for _ in range(t):
    s = "R" + input() + "R"
    res = lst = 0
    for i, c in enumerate(s):
        if c == "R":
            res = max(res, i - lst)
            lst = i
    print(res)
