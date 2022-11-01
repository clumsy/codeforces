t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res = n - sum(1 for i in a if i == min(a))
    print(res)
