t = int(input())
for _ in range(t):
    b, c, h = (int(i) for i in input().split())
    res = min(b - 1, c + h)
    res = 0 if res < 1 else 2 * res + 1
    print(res)
