from math import ceil

t = int(input())
for _ in range(t):
    s = input()
    res = "YES" if s in "Yes" * ceil((len(s) + 2) / 3) else "NO"
    print(res)
