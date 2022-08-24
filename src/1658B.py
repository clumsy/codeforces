MOD = 998244353
t = int(input())
for _ in range(t):
    n = int(input())
    # gcd will only be > 1 for even length, and gcd = 2
    if n & 1 == 1:
        print("0")
        continue
    # we can permute n/2 even numbers for n/2 odd positions, likewise for odd
    # hence res = (n/2)!*(n/2)!
    fac = 1
    for i in range(1, n // 2 + 1):
        fac = (fac * i) % MOD
    res = (fac * fac) % MOD
    print(res)
