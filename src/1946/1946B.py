MOD = 1000000007
t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    a = (int(i) for i in input().split())
    ma = cur = s = 0
    for i in a:
        s += i
        cur = max(0, i, cur + i)
        ma = max(cur, ma)
    res = (s + max(0, ma * (2**k - 1))) % MOD
    print(res)
