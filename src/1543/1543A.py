t = int(input())
for _ in range(t):
    a, b = (int(i) for i in input().split())
    if a == b:
        res = 0, 0
    else:
        a, b = max(a, b), min(a, b)
        max_gcd, moves = a - b, b
        rem = a % max_gcd
        if rem == b % max_gcd:
            moves = min(b, 0 if rem == 0 else min(rem, max_gcd - rem))
        res = max_gcd, moves
    print(*res)
