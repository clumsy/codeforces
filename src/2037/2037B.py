from collections import Counter


t = int(input())
for _ in range(t):
    k, a = int(input()), (int(i) for i in input().split())
    cnt = Counter(a)
    for n in cnt:
        m, r = divmod(k - 2, n)
        if r == 0 and cnt[m] > (n == m):
            res = n, m
            break
    print(*res)
