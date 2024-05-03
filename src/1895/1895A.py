t = int(input())
for _ in range(t):
    x, y, k = (int(i) for i in input().split())
    res = x if y <= x else x + min(y - x, k) + 2 * max(0, y - (x + k))
    print(res)
