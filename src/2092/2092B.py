t = int(input())
for _ in range(t):
    n = int(input())
    a, b = (input() for _ in range(2))
    z = [0] * 2
    for i in range(n):
        z[i & 1] += a[i] == "0"
        z[(i + 1) & 1] += b[i] == "0"
    res = "YES" if z[0] >= (n + 1) // 2 and z[1] >= n // 2 else "NO"
    print(res)
