t = int(input())
for _ in range(t):
    n = int(input())
    res = (
        -1
        if n == 1 or n == 3
        else "3" * (n - 2) + "66"
        if n & 1 == 0
        else "3" * (n - 4) + "6366"
    )
    print(res)
