n = int(input())
for _ in range(n):
    a, b, c, x, y = map(int, input().split())
    print("YES" if max(x - a, 0) + max(y - b, 0) <= c else "NO")
