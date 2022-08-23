t = int(input())
for _ in range(t):
    n = int(input())
    # lcm(1, 1) = 1
    # gcd(1, b) = 1 => b = n - 3
    a, b, c, d = 1, n - 3, 1, 1
    print(a, b, c, d)
