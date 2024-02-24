t = int(input())
for k in range(t):
    a, b = (int(i) for i in input().split())
    res = (
        "NO"
        if a & 1 == b & 1 == 1
        or (a & 1 == 1 and b == 2 * a)
        or (b & 1 == 1 and a == 2 * b)
        else "YES"
    )
    print(res)
