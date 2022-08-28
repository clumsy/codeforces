t = int(input())
for _ in range(t):
    n = int(input())
    if n & 1:  # sum is always even for any a, b, c
        print(-1)
    else:
        a, b, c = 0, 0, n // 2
        print(a, b, c)
