t = int(input())
for _ in range(t):
    n, k, d, w = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    res = rem = cur = 0
    for i in a:
        if i > cur or rem == 0:
            res += 1
            cur = i + d + w
            rem = k
        rem -= 1
    print(res)
