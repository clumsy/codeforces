t = int(input())
for _ in range(t):
    a = [int(i) for i in input().split()]

    def dfs(cur):
        if cur > 7:
            return 0
        res = dfs(cur + 1)
        has = all(a[i] > 0 for i in range(3) if cur & (1 << i) == (1 << i))
        if has:
            for i in range(3):
                if cur & (1 << i) == (1 << i):
                    a[i] -= 1
            res = max(res, 1 + dfs(cur + 1))
            for i in range(3):
                if cur & (1 << i) == (1 << i):
                    a[i] += 1
        return res

    res = dfs(1)

    print(res)
