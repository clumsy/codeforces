t = int(input())
for _ in range(t):
    x, y, a, b = (int(i) for i in input().split())
    time = (y - x) // (a + b)
    res = x + a * time == y - b * time
    print(time if res else -1)
