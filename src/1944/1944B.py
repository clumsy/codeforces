from collections import Counter


t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    cnt = Counter(next(a) for _ in range(n))
    res1 = []
    res2 = []
    mis = [i for i in range(1, n + 1) if i not in cnt]
    for i, c in cnt.items():
        if len(res1) == 2 * k:
            break
        if c == 2:
            res1.append(i)
            res1.append(i)
            i = mis.pop()
            res2.append(i)
            res2.append(i)
    for i, c in cnt.items():
        if len(res1) == 2 * k:
            break
        if c == 1:
            res1.append(i)
            res2.append(i)
    print(*res1)
    print(*res2)
