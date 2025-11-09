from collections import Counter


t = int(input())
for _ in range(t):
    n, s, t = int(input()), *input().split()
    res = "YES" if Counter(s) == Counter(t) else "NO"
    print(res)
