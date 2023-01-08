t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res, cnt = [""] * n, 0
    for i, d in enumerate(s):
        cnt += d == "1"
        if i > 0:
            v = "+"
            if d == "1" and cnt > 0:
                v = "-"
                cnt -= 2
            res[i] = v
    res = "".join(res)
    print(res)
