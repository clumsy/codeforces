t = int(input())
for _ in range(t):
    n, a = int(input()), sorted(int(i) for i in input().split())
    res = sum(a[2 * i] for i in range(n))
    print(res)
