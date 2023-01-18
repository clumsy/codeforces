t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res = max(ord(c) for c in s) - ord("a") + 1
    print(res)
