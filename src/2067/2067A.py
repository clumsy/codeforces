t = int(input())
for _ in range(t):
    x, y = (int(i) for i in input().split())
    res = "YES" if (y < x and (x + 1 - y) % 9 == 0) or y - x == 1 else "NO"
    print(res)
