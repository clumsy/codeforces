t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    s = sorted(a)
    res = "YES" if all((a[i] & 1) == (s[i] & 1) for i in range(n)) else "NO"
    print(res)
