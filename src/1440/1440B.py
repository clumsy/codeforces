t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = [int(i) for i in input().split()]
    step = -((n + 2) // 2)
    r = a[step : step * k - 1 : step]
    res = sum(r)
    print(res)
