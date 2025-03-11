t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res = int(s[0] == "1")
    for i in range(1, n):
        res += s[i] != s[i - 1]
    print(res)
