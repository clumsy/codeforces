t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res = "YES"
    for i in range(1, n, 3):
        if len(s) <= i + 1 or s[i + 1] != s[i]:
            res = "NO"
            break
    print(res)
