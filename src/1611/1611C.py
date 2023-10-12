t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    ma = max(a)
    if a[0] == ma:
        res = a[1:][::-1] + [ma]
    elif a[-1] == ma:
        res = a[:-1][::-1] + [ma]
    else:
        res = [-1]
    print(*res)
