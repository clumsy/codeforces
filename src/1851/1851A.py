t = int(input())
for _ in range(t):
    n, m, k, H = (int(i) for i in input().split())
    h = (int(i) for i in input().split())
    res = 0
    for i in h:
        diff = abs(H - i)
        s = diff // k
        res += 0 < s < m and k * s == diff
    print(res)
