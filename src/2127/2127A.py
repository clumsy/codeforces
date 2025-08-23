from collections import Counter


t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    cnt = Counter(a)
    res = "YES" if cnt[0] == 0 and sum(k != -1 for k in cnt) <= 1 else "NO"
    print(res)
