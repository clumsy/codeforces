t = int(input())
for _ in range(t):
    lo, hi = (int(i) for i in input().split())
    # l >= ax + a/2 = a(x + 1/2), r < a(x + 1)
    # let x = 0 => r < a <= 2l
    res = "YES" if hi < 2 * lo else "NO"
    print(res)
