t = int(input())
for _ in range(t):
    n, m, i, j = (int(i) for i in input().split())
    d, corners = 0, [(1, 1), (n, 1), (1, m), (n, m)]
    res = i, j, i, j
    for p1 in corners:
        for p2 in corners:
            cur_d = (
                abs(i - p1[0])
                + abs(j - p1[1])
                + abs(p1[0] - p2[0])
                + abs(p1[1] - p2[1])
                + abs(i - p2[0])
                + abs(j - p2[1])
            )
            if cur_d > d:
                d, res = cur_d, p1 + p2
    print(*res)
