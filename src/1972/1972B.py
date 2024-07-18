t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res = "YES" if s.count("U") & 1 == 1 else "NO"
    print(res)
