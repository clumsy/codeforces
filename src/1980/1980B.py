t = int(input())
for _ in range(t):
    n, f, k = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    f -= 1
    hi = eq = 0
    for i in a:
        hi += i > a[f]
        eq += i == a[f]
    res = "YES" if k >= hi + eq else "MAYBE" if k > hi else "NO"
    print(res)
