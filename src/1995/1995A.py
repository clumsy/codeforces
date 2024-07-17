t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    res = 0
    for i in reversed(range(1, n + 1)):
        if k <= 0:
            break
        res += 1
        k -= i
        if k <= 0:
            break
        if i != n:
            res += 1
            k -= i
    print(res)
