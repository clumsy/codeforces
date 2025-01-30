t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    res = 0
    input()  # the first one does not matter
    for _ in range(n - 1):
        x, y = (int(i) for i in input().split())
        res += x + y
    res = 2 * (res + 2 * m)
    print(res)
