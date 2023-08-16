t = int(input())
for _ in range(t):
    n = int(input())
    # 10 1 -> 6
    # 9 2 -> 6
    # 8 3 -> 6
    # 7 4 -> 6
    # 6 5 -> 6
    res = 2
    print(res)
    print(n, n - 1)
    for i in range(n - 2):
        print(n - i, n - i - 2)
