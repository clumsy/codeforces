t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res = "YES" if s[0] != s[-1] else "NO"
    print(res)
