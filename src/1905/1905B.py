t = int(input())
for _ in range(t):
    n = int(input())
    cnt = [0] * n
    for _ in range(n - 1):
        u, v = (int(i) for i in input().split())
        cnt[u - 1] += 1
        cnt[v - 1] += 1
    res = (sum(v == 1 for v in cnt) + 1) // 2
    print(res)
