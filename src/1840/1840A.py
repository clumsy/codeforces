t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res, i = [], 0
    while i < n:
        res.append(s[i])
        i += 1
        while i < n and s[i] != res[-1]:
            i += 1
        i += 1
    res = "".join(res)
    print(res)
