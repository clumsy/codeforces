t = int(input())
for _ in range(t):
    a, b, c = sorted(int(i) for i in input().split())
    k = 3
    while k and b > a:
        b -= a
        k -= 1
    while k and c > a:
        c -= a
        k -= 1
    res = "YES" if a == b == c else "NO"
    print(res)
