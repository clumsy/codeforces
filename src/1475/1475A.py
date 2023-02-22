t = int(input())
for _ in range(t):
    n = int(input())
    # if not power of 2 will always have an odd divisor
    res = "YES" if n - (n & -n) != 0 else "NO"
    print(res)
