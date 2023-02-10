t = int(input())
for _ in range(t):
    n = int(input())
    a, b = [0] * n, [0] * n
    for i in range(n):
        a[i], b[i] = (int(i) for i in input().split())
        a[i], b[i] = min(a[i], b[i]), max(a[i], b[i])
    b.sort()
    res = 2 * sum(a) + b[0] + b[-1] + sum(b[i] - b[i - 1] for i in range(1, n))
    print(res)
