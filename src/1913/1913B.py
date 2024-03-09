from collections import Counter


t = int(input())
for _ in range(t):
    s = [int(i) for i in input()]
    cnt = Counter(s)
    res, n = 0, len(s)
    for i in range(n):
        if cnt[1 - s[i]]:
            cnt[1 - s[i]] -= 1
        else:
            res += n - i
            break
    print(res)
