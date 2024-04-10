t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res = "YES" if s.count("1") != n else "NO"
    print(res)
