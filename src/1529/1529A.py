t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res = n - a.count(min(a))
    print(res)
