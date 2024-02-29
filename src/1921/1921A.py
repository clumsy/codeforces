t = int(input())
for _ in range(t):
    m = {}
    for _ in range(4):
        x, y = (int(i) for i in input().split())
        m[x] = m.get(x, [])
        m[x].append(y)
        if len(m[x]) == 2:
            res = abs(m[x][0] - m[x][1]) ** 2
    print(res)
