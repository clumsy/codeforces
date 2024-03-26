t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    a.sort()
    res = 1
    m = (n + 1) // 2 - 1
    while m + res < n and a[m + res] == a[m]:
        res += 1
    print(res)
