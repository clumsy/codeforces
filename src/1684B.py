t = int(input())
for _ in range(t):
    a, b, c = (int(i) for i in input().split())
    z = c
    y = z + b
    x = y + a
    print(x, y, z)
