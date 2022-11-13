t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res = "YES" if a[0] == min(a) else "NO"
    print(res)
