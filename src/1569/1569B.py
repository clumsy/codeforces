t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    if s.count("2") not in {1, 2}:
        print("YES")
        res = [list("=" * i + "X" + "=" * (n - 1 - i)) for i in range(n)]
        prv = None
        for i in range(n):
            if s[i] == "2":
                if prv is not None:
                    res[prv][i] = "+"
                    res[i][prv] = "-"
                    prv = i
                else:
                    fst = prv = i
        if prv is not None:
            res[prv][fst] = "+"
            res[fst][prv] = "-"
        for res in res:
            print("".join(res))
    else:
        print("NO")
