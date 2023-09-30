t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    s = input()
    res, p = 0, None
    for i, e in enumerate(s):
        if e == "B" and (p is None or i - p >= k):
            res += 1
            p = i
    print(res)
