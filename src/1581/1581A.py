MOD = 1000000007
t = int(input())
for _ in range(t):
    n = int(input())
    res = 1
    # of all 2*n permutations half satisfies the condition, hence:
    # res = (2 * n)! / 2
    for i in range(3, 2 * n + 1):
        res = (res * i) % MOD
    print(res)
