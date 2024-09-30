t = int(input())
for _ in range(t):
    n, k = (int(i) for i in input().split())
    res = (
        "YES"
        if 4 * (k // 4) == k or (k & 1 == 1 and n & 1 == (((k - 1) // 2) & 1))
        else "NO"
    )
    print(res)
