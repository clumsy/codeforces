t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    r = sum(a) % n
    res = (n - r) * r
    print(res)
