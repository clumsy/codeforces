t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    pls = s.count("+")
    res = abs(pls - (n - pls))
    print(res)
