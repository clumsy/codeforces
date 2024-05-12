from collections import Counter


t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    c = (int(i) for i in input().split())
    res = n
    for v in Counter(c).values():
        if v >= k:
            res = k - 1
            break
    print(res)
