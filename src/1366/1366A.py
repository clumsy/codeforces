t = int(input())
for _ in range(t):
    a, b = sorted(int(i) for i in input().split())
    d = min(b - a, a)
    res = d
    a, b = a - d, b - 2 * d
    c = min(a, b)
    c -= c % 3
    res += 2 * (c // 3)
    a, b = a - c, b - c
    res += min(b // 2, a)
    print(res)
