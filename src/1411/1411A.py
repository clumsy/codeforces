t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res = "Yes" if n > 2 * len(s.rstrip(")")) else "No"
    print(res)
