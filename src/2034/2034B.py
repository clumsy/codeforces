t = int(input())
for _ in range(t):
    n, m, k = (int(i) for i in input().split())
    s = input()
    res, cur = 0, m
    for c in s:
        cur = max(cur - 1, m) if c == "1" else cur - 1
        if cur == 0:
            res += 1
            cur = k + m - 1
    print(res)
