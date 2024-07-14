from collections import Counter


t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    g = [[int(i) for i in input().split()] for _ in range(n)]
    cnt = Counter()
    for r in range(n):
        for c in range(m):
            cnt[g[r][c]] += 1
    res = [[0] * m for _ in range(n)]
    for r in range(n):
        for c in range(m):
            for k in range(g[r][c] + 1, n * m + 1):
                if cnt[k] > 0 and k != g[r][c]:
                    res[r][c] = k
                    cnt[k] -= 1
                    break
            else:
                for k in range(1, g[r][c]):
                    if cnt[k] > 0 and k != g[r][c]:
                        res[r][c] = k
                        cnt[k] -= 1
                        break
                else:
                    res = -1
                    break
        if res == -1:
            break
    if res == -1:
        print(res)
    else:
        for r in res:
            print(*r)
