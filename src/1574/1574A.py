t = int(input())
for _ in range(t):
    n = int(input())
    res = []

    def dfs(cur, o):
        if len(res) == n:
            return
        if len(cur) == 2 * n:
            res.append("".join(cur))
            return
        if o < n:
            cur.append("(")
            dfs(cur, o + 1)
            cur.pop()
        if o > 0:
            cur.append(")")
            dfs(cur, o)
            cur.pop()

    dfs([], 0)
    print(*res, sep="\n")
