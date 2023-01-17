t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    res = a = [int(i) for i in input().split()]
    lo, hi = 0, 0
    for i in range(n):
        lo = i if a[i] < a[lo] else lo
        hi = i if a[i] > a[hi] else hi
    d, ma, even = a[hi], a[hi] - a[lo], k & 1 == 0
    for i in range(n):
        if i == lo:
            a[i] = 0 if even else ma
        elif i == hi:
            a[i] = ma if even else 0
        else:
            a[i] = ma - (d - a[i]) if even else d - a[i]
    print(*res)
