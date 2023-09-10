from collections import Counter

t = int(input())
for _ in range(t):
    n, s = int(input()), input()
    res, lft, rgt = 0, Counter(), Counter(s)
    for c in s:
        lft[c] += 1
        rgt[c] -= 1
        if rgt[c] == 0:
            del rgt[c]
        res = max(res, len(lft) + len(rgt))
    print(res)
