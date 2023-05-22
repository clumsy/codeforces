t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res = len({s[i : i + 2] for i in range(n - 1)})
    print(res)
