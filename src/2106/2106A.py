t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res = sum(n - 1 if c == "1" else 1 for c in s)
    print(res)
