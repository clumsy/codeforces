from collections import Counter


t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res, cnt = "NO", Counter(s)
    for i in range(1, n - 1):
        if cnt[s[i]] > 1:
            res = "YES"
            break
    print(res)
