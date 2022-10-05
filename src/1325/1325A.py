t = int(input())
for _ in range(t):
    x = int(input())
    # gcd(x-1,1) + lcm(x-1,1) = 1 + x - 1 = x
    res = x - 1, 1
    print(*res)
