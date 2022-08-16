t = int(input())
for _ in range(t):
    n, m = (int(i) for i in input().split())
    n, m = max(n, m), min(n, m)  # n > m
    if n == 1 and m == 1:
        x = 0
    elif n > 2 and m == 1:
        x = -1
    else:  # min(n, m) >= 2
        x = 2 * (m - 1)  # now at (m, m), always come from left
        x += 4 * ((n - m) // 2) + ((n - m) % 2)
    print(x)
