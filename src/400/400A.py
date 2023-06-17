t = int(input())
for _ in range(t):
    s = input()
    res, n = [], len(s)
    for a in [1, 2, 3, 4, 6, 12]:
        b = 12 // a
        for i in range(b):
            if all(s[j] == "X" for j in range(i, n, b)):
                res.append(f"{a}x{b}")
                break
    if res:
        print(len(res), *res)
    else:
        print("0")
