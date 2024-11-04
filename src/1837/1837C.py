t = int(input())
for _ in range(t):
    s = input()
    res = list(s)
    p = "0"
    for i, c in enumerate(s):
        if c == "?":
            res[i] = p
        else:
            p = c
    res = "".join(res)
    print(res)
