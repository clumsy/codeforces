from collections import Counter


t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    cnt = Counter(s)
    res = sum(min(n, cnt[c]) for c in "ABCD")
    print(res)
