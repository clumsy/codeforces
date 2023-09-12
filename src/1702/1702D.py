t = int(input())
for _ in range(t):
    w, p = list(input()), int(input())
    n, a, res = len(w), ord("a") - 1, 0
    order = sorted(range(n), key=w.__getitem__)
    s = sum(ord(c) for c in w) - n * a
    while res < n and p < s:
        res += 1
        i = order[n - res]
        s -= ord(w[i]) - a
        w[i] = ""
    res = "".join(w)
    print(res)
