t = int(input())
for _ in range(t):
    n, a = int(input()), [int(i) for i in input().split()]
    res = "NO" if a[-1] - a[0] == 0 else "YES"
    print(res)
    if res == "YES":
        print("RB" + "R" * (n - 2))
