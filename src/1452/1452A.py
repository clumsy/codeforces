t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    res = 2 * max(x, y) - (x != y)
    print(res)
