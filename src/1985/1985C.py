t = int(input())
for _ in range(t):
    n, a = int(input()), (int(i) for i in input().split())
    res = s = m = 0
    for i in a:
        m = max(m, i)
        s += i
        res += s == 2 * m
    print(res)
