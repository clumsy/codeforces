t = int(input())
for _ in range(t):
    m, a, b, c = (int(i) for i in input().split())
    res = min(m, a) + min(m, b)
    res += min(c, 2 * m - res)
    print(res)
