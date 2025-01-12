t = int(input())
for _ in range(t):
    n = int(input())
    res = 1
    while n > 3:
        res *= 2
        n //= 4
    print(res)
