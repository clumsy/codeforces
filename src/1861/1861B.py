t = int(input())
for _ in range(t):
    a, b = (list(input()) for _ in range(2))
    res = "NO"
    i_ = j_ = False
    for i, j in zip(a, b):
        if not i_ and not j_ and i == j == "1":
            res = "YES"
            break
        i_ = i == "1"
        j_ = j == "1"
    print(res)
