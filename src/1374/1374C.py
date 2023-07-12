t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res = o = c = 0
    for i in s:
        o += i == "("
        c += i == ")"
        res = max(res, c - o)
    print(res)
