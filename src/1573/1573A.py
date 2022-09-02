t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res = sum(int(d) + (1 if d != "0" and i != n - 1 else 0) for i, d in enumerate(s))
    print(res)
