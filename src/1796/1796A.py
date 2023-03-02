t = int(input())
for _ in range(t):
    k, s = int(input()), input()
    res = "YES" if s in "BFFBFFBF" * 3 else "NO"
    print(res)
