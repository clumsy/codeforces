t = int(input())
for _ in range(t):
    n, d = list(input().split())
    s = input()
    i = next((i for i, c in enumerate(s) if c < d), int(n))
    res = s[:i] + d + s[i:]
    print(res)
