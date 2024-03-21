t = int(input())
for _ in range(t):
    n, a = int(input()), sorted(int(i) for i in input().split())
    m1 = a[-1] - a[0] + abs(a[0] - a[-2]) + a[-2] - a[1] + a[-1] - a[1]
    m2 = abs(a[0] - a[-1]) + a[-1] - a[1] + abs(a[1] - a[-2]) + a[-2] - a[0]
    res = max(m1, m2)
    print(res)
