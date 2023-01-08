t = int(input())
for _ in range(t):
    m = [[int(i) for i in input().split()] for _ in range(2)]
    mi = sorted([m[0][0], m[0][1], m[1][0], m[1][1]])[0]
    while m[0][0] != mi:
        m[0][0], m[0][1], m[1][1], m[1][0] = m[1][0], m[0][0], m[0][1], m[1][1]
    res = (
        "YES" if (m[0][0] < m[0][1] < m[1][1] and m[0][0] < m[1][0] < m[1][1]) else "NO"
    )
    print(res)
