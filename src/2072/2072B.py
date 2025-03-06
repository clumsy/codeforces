t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    d = u = 0
    for c in s:
        d += c == "-"
        u += c == "_"
    l, m, r = d // 2, u, d // 2 + (d & 1)
    res = l * m * r
    print(res)
