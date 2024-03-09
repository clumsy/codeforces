t = int(input())
for _ in range(t):
    s = input()
    lo, up = [], []
    for i, c in enumerate(s):
        if c == "b":
            if lo:
                lo.pop()
        elif c == "B":
            if up:
                up.pop()
        elif c.islower():
            lo.append(i)
        else:
            up.append(i)
    res = []
    while lo or up:
        l_ = lo[-1] if lo else -1
        u_ = up[-1] if up else -1
        if u_ > l_:
            res.append(s[up.pop()])
        else:
            res.append(s[lo.pop()])
    res = "".join(res[::-1])
    print(res)
