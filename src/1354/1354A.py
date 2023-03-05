t = int(input())
for _ in range(t):
    a, b, c, d = (int(i) for i in input().split())
    res = b
    a -= min(a, b)
    if a > 0:
        diff = c - d
        if diff <= 0:
            res = -1
        else:
            res += c * ((a + diff - 1) // diff)
    print(res)
