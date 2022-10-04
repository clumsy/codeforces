t = int(input())
for _ in range(t):
    n = input()
    res, zs = [], ""
    for i in reversed(n):
        if i != "0":
            res.append(i + zs)
        zs += "0"
    print(len(res))
    print(*res)
