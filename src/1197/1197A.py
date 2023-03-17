t = int(input())
for _ in range(t):
    n, a = int(input()), sorted((int(i) for i in input().split()), reverse=True)
    k = a[1] - 1
    res = min(a[1] - 1, n - 2)
    print(res)
