t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    res = cur = mab = 0
    for i in range(min(n, k)):
        cur += a[i]
        mab = max(mab, b[i])
        res = max(res, cur + (k - 1 - i) * mab)
    print(res)
