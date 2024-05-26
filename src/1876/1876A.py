t = int(input())
for _ in range(t):
    n, p = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    ord = sorted(range(n), key=b.__getitem__)
    res = k = 0
    for o, i in enumerate(ord):
        if k <= o:
            k += 1
            res += p
        if b[i] < p:
            cnt = min(n - k, a[i])
            res += b[i] * cnt
            k += cnt
        if k == n:
            break
    print(res)
