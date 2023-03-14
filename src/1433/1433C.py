t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    mi, ma = 0, 0
    for i in range(1, n):
        mi = mi if a[mi] <= a[i] else i
        if a[i] > a[ma] or (
            a[i] == a[ma] and (a[i - 1] < a[i] or (i < n - 1 and a[i + 1] < a[i]))
        ):
            ma = i
    res = -1 if a[mi] == a[ma] else ma + 1
    print(res)
