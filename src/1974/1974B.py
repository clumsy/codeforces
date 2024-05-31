t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    unq, m = sorted(set(s)), {}
    for i, e in enumerate(unq):
        m[e] = unq[len(unq) - 1 - i]
    res = "".join(m[c] for c in s)
    print(res)
