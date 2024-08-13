t = int(input())
for _ in range(t):
    n, a = int(input()), sorted(int(i) for i in input().split())
    res = a[n // 2]
    print(res)
