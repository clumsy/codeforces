t = int(input())
for _ in range(t):
    n = int(input())
    res = 1 + 3 * (n // 15) + min(2, n % 15)
    print(res)
