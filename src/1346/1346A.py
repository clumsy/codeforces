t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    # n1 + n1 * k + n1 * k^2 + n1 * k ^ 3 = n
    # n1 = n / (1 + k + k^2 + k^3)
    n1 = n // (1 + k + k**2 + k**3)
    res = n1, n1 * k, n1 * k**2, n1 * k**3
    print(*res)
