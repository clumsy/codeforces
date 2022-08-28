t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    for i in range(n):
        a[i], b[i] = min(a[i], b[i]), max(a[i], b[i])
    res = 0
    res += sum(abs(i - j) for i, j in zip(a[:-1], a[1:]))
    res += sum(abs(i - j) for i, j in zip(b[:-1], b[1:]))
    print(res)
