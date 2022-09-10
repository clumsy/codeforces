t = int(input())
for _ in range(t):
    n = int(input())
    c1, c2 = n // 3 + (n % 3 == 1), n // 3 + (n % 3 == 2)
    print(c1, c2)
