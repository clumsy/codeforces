t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res = cur = 1
    for i in range(1, n):
        if s[i] != s[i - 1]:
            cur = 0
        cur += 1
        res = max(res, cur)
    res += 1
    print(res)
