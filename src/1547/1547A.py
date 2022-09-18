t = int(input())
for _ in range(t):
    input()
    a, b, f = [[int(i) for i in input().split()] for _ in range(3)]
    res = abs(a[0] - b[0]) + abs(a[1] - b[1])
    if (a[0] == b[0] == f[0] and min(a[1], b[1]) < f[1] < max(a[1], b[1])) or (
        a[1] == b[1] == f[1] and min(a[0], b[0]) < f[0] < max(a[0], b[0])
    ):
        res += 2
    print(res)
