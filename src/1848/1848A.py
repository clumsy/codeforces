t = int(input())
for _ in range(t):
    n, m, k = (int(i) for i in input().split())
    res = "YES"
    a, b = (int(i) for i in input().split())
    for _ in range(k):
        x, y = (int(i) for i in input().split())
        if (abs(x - a) + abs(y - b)) & 1 == 0:
            res = "NO"
    print(res)
