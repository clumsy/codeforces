t = int(input())
for _ in range(t):
    n = int(input())
    # last is X, optimal to have X.X in the middle
    n -= 4
    # rest divide evenly in 3 parts
    l1, l2 = 1, (n + 2) // 3  # ceil
    l3 = n - l2
    res = min(abs(l1 - l2), abs(l2 - l3), abs(l1 - l3))
    print(res)
