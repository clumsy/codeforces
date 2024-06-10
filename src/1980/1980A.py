from collections import Counter


t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    a = input()
    cnt = Counter(a)
    res = sum(max(0, m - cnt[c]) for c in "ABCDEFG")
    print(res)
