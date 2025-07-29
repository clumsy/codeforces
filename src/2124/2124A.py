t = int(input())
for _ in range(t):
    k, d = int(input()), (int(i) for i in input().split())
    res, p = ["NO"], next(d)
    for i in d:
        if p > i:
            res = ["YES", 2, f"{p} {i}"]
        p = i
    print(*res, sep="\n")
