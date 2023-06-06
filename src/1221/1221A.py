from collections import Counter

q = int(input())
for _ in range(q):
    n, s = int(input()), Counter(int(i) for i in input().split())
    for i in range(12):
        s[2 ** (i + 1)] += s[2**i] // 2
    res = "YES" if s[2048] > 0 else "NO"
    print(res)
