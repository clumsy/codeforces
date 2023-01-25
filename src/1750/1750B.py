t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res, cur = 0, 1
    for i in range(1, n):
        if s[i] == s[i - 1]:
            cur += 1
        else:
            res, cur = max(res, cur), 1
    res = max(res * res, cur * cur, (z := s.count("0")) * (n - z))
    print(res)
