t = int(input())
for _ in range(t):
    n, a, b, c = (int(i) for i in input().split())
    d, n = divmod(n, a + b + c)
    res = 3 * d + (0 if n == 0 else 1 if n <= a else 2 if n <= a + b else 3)
    print(res)
