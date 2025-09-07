t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    a = sorted(a, reverse=True)
    res = sum(a[::2])
    print(res)
