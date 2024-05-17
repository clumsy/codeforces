n, a = int(input()), (int(i) for i in input().split())
a = sorted(a)
x = sum(a) // n
for i in range(n):
    res = a[i], x - a[i]
    print(*res)
