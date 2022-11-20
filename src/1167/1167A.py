t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res = "YES" if n >= n - s.find("8") >= 11 else "NO"
    print(res)
