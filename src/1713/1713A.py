t = int(input())
for _ in range(t):
    n = int(input())
    max_y = min_y = max_x = min_x = 0
    for i in range(n):
        x, y = map(int, input().split())
        max_y, min_y = max(max_y, y), min(min_y, y)
        max_x, min_x = max(max_x, x), min(min_x, x)
    print(2 * (max_x + max_y + -min_x + -min_y))
