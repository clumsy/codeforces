n = int(input())
for _ in range(n):
    a, b = (int(i) for i in input().split())
    # x * a + y * a = z * a * b
    # x = 1, y = b - 1
    if b == 1:
        print("NO")
    else:
        print("YES")
        if b == 2:
            res = 2 * a, 3 * a, 5 * a
        else:
            res = a, (b - 1) * a, a * b
        print(*res)
