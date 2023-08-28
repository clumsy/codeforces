t = int(input())
for _ in range(t):
    res = []
    for _ in range(8):
        for c in input():
            if c != ".":
                res.append(c)
                break
    res = "".join(res)
    print(res)
